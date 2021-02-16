import logging
from typing import Tuple, Type, TypeVar

from newversion import Version

from logchange.record_body import RecordBody
from logchange.utils import dedent

_R = TypeVar("_R", bound="Record")


class Record:
    PARTS_DELIM = "\n"

    def __init__(
        self,
        version: Version,
        body: RecordBody,
        created: str,
    ):
        self.version = version
        self.created = created
        self.body = body
        self.logger = logging.getLogger("logchange")

    @property
    def name(self) -> str:
        if self.version == Version.zero():
            return "[Unreleased]"

        return f"[{self.version.dumps()}]"

    def _render_title(self) -> str:
        if self.version == Version.zero():
            return "## [Unreleased]"

        if self.created:
            return f"## [{self.version}] - {self.created}"

        return f"## [{self.version}]"

    def render(self) -> str:
        parts = [self._render_title(), self.body.render()]
        parts = [i for i in parts if i]
        return self.PARTS_DELIM.join(parts)

    @staticmethod
    def _parse_title(title: str) -> Tuple[str, str]:
        title_parts = title.split()
        version = (
            title_parts[1].replace("[", "").replace("]", "") if len(title_parts) > 1 else "0.0.0"
        )
        created = title_parts[3] if len(title_parts) > 3 else ""
        return (version, created)

    @classmethod
    def parse(cls: Type[_R], text: str) -> _R:
        text = dedent(text)
        if not text:
            return cls(Version.zero(), created="", body=RecordBody())

        try:
            title, lines = text.split("\n", 1)
        except ValueError:
            title = text
            lines = ""

        version, created = cls._parse_title(title)
        return cls(
            version=Version(version),
            created=created,
            body=RecordBody.parse(lines),
        )

    def is_empty(self) -> bool:
        return self.body.is_empty()

    def set_section(self, title: str, body: str) -> None:
        section = self.body.get_section(title)
        was_empty = section.is_empty()
        section.body = body
        self.body.set_section(title, body)
        if was_empty:
            if body:
                self.logger.info(f"{self.name} `{section.name}` section added")
        else:
            if body:
                self.logger.info(f"{self.name} `{section.name}` section overwritten")
            else:
                self.logger.info(f"{self.name} `{section.name}` section deleted")

    def append_section(self, title: str, body: str) -> None:
        section = self.body.get_section(title)
        was_empty = section.is_empty()
        section.append_lines(body)
        if was_empty:
            if body:
                self.logger.info(f"{self.name} `{section.name}` section added")
        elif body:
            self.logger.info(f"{self.name} `{section.name}` section updated")

    def set_body(self, text: str) -> None:
        new_body = RecordBody.parse(text)
        for section in new_body.sections.values():
            self.set_section(section.title, section.body)

    def merge_body(self, text: str) -> None:
        new_body = RecordBody.parse(text)
        for section in new_body.sections.values():
            self.append_section(section.title, section.body)
