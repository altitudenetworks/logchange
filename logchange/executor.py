"""
CLI commands executor.
"""
import argparse
import logging
from pathlib import Path

from newversion import Version

from logchange.changelog import ChangeLog
from logchange.constants import (
    AUTO,
    LATEST,
    NEW_CHANGELOG,
    SECTION_ALL,
    UNRELEASED,
)
from logchange.eol_fixer import EOLFixer
from logchange.record import Record
from logchange.record_body import RecordBody
from logchange.utils import print_path


class ExecutorError(Exception):
    """
    Main CLI commands executor error.
    """


class Executor:
    """
    CLI commands executor.
    """

    def __init__(self, config: argparse.Namespace) -> None:
        self.config = config
        self.windows_le = False
        self.logger = logging.getLogger("logchange")

    @property
    def input(self) -> str:
        self.windows_le = EOLFixer.is_windows(self.config.input)
        return EOLFixer.to_unix(self.config.input)

    @property
    def changelog_path(self) -> Path:
        return self.config.changelog_path

    @property
    def changelog(self) -> ChangeLog:
        if not self.changelog_path.exists():
            self.logger.info(
                f"{print_path(self.changelog_path)} does not exists, generated a new one."
            )
            return ChangeLog.parse(NEW_CHANGELOG)

        text = self.changelog_path.read_text()
        self.windows_le = EOLFixer.is_windows(text)
        return ChangeLog.parse(EOLFixer.to_unix(text))

    def save_changelog(self, changelog: ChangeLog) -> None:
        self.changelog_path.write_text(self._fix_eol(changelog.render()))

    @property
    def release_name(self) -> str:
        return self.config.name

    def _fix_eol(self, text: str) -> str:
        if not self.windows_le:
            return text

        return EOLFixer.to_windows(text)

    @staticmethod
    def _as_md_list(text: str) -> str:
        if not text.strip():
            return text

        if "\n" in text:
            return text

        if text.strip().startswith("-"):
            return text

        return f"- {text}"

    def execute(self) -> str:
        """
        Execute command based on `config`.

        Returns:
            String output.
        """
        commands = dict(
            init=self._command_init,
            add=self._command_add,
            get=self._command_get,
            format=self._command_format,
            list=self._command_list,
            version=self._command_version,
        )
        command = self.config.command
        if command not in commands:
            raise ExecutorError("Unknown command")

        return self._fix_eol(commands[self.config.command]())

    def _command_init(self) -> str:
        if not self.changelog_path.exists():
            self.changelog_path.write_text(NEW_CHANGELOG)
            self.logger.info(f"{print_path(self.changelog_path)} created successfully.")
            return ""

        if not self.config.format:
            self.logger.info(
                f"{print_path(self.changelog_path)} already exists."
                " Add `-f` to reformat it."
            )
            return ""

        text = self.changelog_path.read_text()
        self.windows_le = EOLFixer.is_windows(text)
        changelog = ChangeLog.parse(EOLFixer.to_unix(text))
        changelog.format_released()
        new_text = changelog.render()
        if new_text == text:
            self.logger.info(
                f"{print_path(self.changelog_path)} is good as it is, you are doing great!"
            )
            return ""

        self.changelog_path.write_text(self._fix_eol(changelog.render()))
        self.logger.info(f"{print_path(self.changelog_path)} reformatted.")
        return ""

    def _command_add(self) -> str:
        release_name = self.release_name
        changelog = self.changelog
        if release_name == UNRELEASED:
            record = changelog.get_unreleased()
        elif release_name == LATEST:
            record = changelog.get_latest()
            if not record:
                raise ExecutorError(
                    f"No releases found in {print_path(self.changelog_path)}, pass explicit version"
                )
        else:
            record = changelog.get_record(Version(release_name))

        if not record:
            self.logger.info(f"Record {release_name} not found, added")
            record = Record(
                version=Version(release_name),
                body=RecordBody(),
                created=self.config.created,
            )

        if self.config.section == SECTION_ALL:
            record_body = RecordBody.parse(self.input)
            record.body = record.body.merge(record_body)
            self.logger.info(f"Record {record.name} section updated")
        else:
            section_name = self.config.section
            record.body.append_lines(section_name, self._as_md_list(self.input))
            self.logger.info(
                f"Record {record.name} {section_name.capitalize()} section updated"
            )

        changelog.update_release(record)
        self.save_changelog(changelog)
        return ""

    def _command_get(self) -> str:
        changelog = self.changelog
        record_name = self.config.name
        if record_name == UNRELEASED:
            record = changelog.get_unreleased()
        elif record_name == LATEST:
            record = changelog.get_latest()
        else:
            record = changelog.get_record(Version(record_name))

        if record is None:
            return ""

        if self.config.section == SECTION_ALL:
            return record.render()
        section = record.body.get_section(self.config.section)
        if section:
            return section.body

        return ""

    def _command_format(self) -> str:
        record_body = RecordBody.parse(self.input)
        return record_body.render()

    def _command_list(self) -> str:
        records = list(self.changelog.iterate_records())
        return "\n".join([i.version.dumps() for i in records])

    def _command_version(self) -> str:
        old_version: Version = self.config.version
        record_body = RecordBody.parse(self.input)
        return record_body.bump_version(old_version).dumps()
