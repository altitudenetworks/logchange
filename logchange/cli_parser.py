"""
Main CLI parser.
"""
import argparse
import sys
from pathlib import Path
from typing import Sequence

import pkg_resources
from newversion import Version, VersionError

from logchange.constants import LATEST, SECTION_ALL, SECTION_TITLES, UNRELEASED


def get_existing_path(value: str) -> Path:
    path = Path(value)
    if not path.exists():
        raise argparse.ArgumentTypeError(f"Path {path} des not exist")
    return path


def get_version_latest_or_unreleased(value: str) -> str:
    value = value.lower()
    if value == UNRELEASED:
        return value

    if value == LATEST:
        return value

    try:
        return Version(value).dumps()
    except VersionError as e:
        raise argparse.ArgumentTypeError(e) from None


def get_stdin() -> str:
    """
    Get input from stdin.

    Returns:
        Parsed version.
    """
    if sys.stdin.isatty():
        return ""

    return sys.stdin.read()


def parse_args(args: Sequence[str]) -> argparse.Namespace:
    """
    Main CLI parser.

    Returns:
        Argument parser Namespace.
    """
    try:
        version = pkg_resources.get_distribution("logchange").version
    except pkg_resources.DistributionNotFound:
        version = "0.0.0"

    parser = argparse.ArgumentParser(
        "logchange",
        description="Keep-a-changelog manager",
    )
    parser.add_argument("-V", "--version", action="version", version=version, help="Show version")
    subparsers = parser.add_subparsers(help="Available subcommands", dest="command")

    parser_init = subparsers.add_parser("init", help="Create CHANGELOG.md")
    parser_init.add_argument(
        "-p",
        "--changelog-path",
        type=Path,
        default=Path.cwd() / "CHANGELOG.md",
        help="Full path to changelog file. Default: ./CHANGELOG.md",
    )
    parser_init.add_argument(
        "-f",
        "--format",
        action="store_true",
        help="Format existing changelog and write back",
    )

    parser_add = subparsers.add_parser("add", help="Add or update a record in CHANGELOG.md")
    parser_add.add_argument(
        "name",
        type=get_version_latest_or_unreleased,
        default=LATEST,
        help="Release name: version, `latest` or `unreleased`",
    )
    parser_add.add_argument(
        "section",
        help="Section name or `All`",
        nargs="?",
        type=lambda x: x.lower(),
        default=SECTION_ALL,
        choices=[SECTION_ALL, *SECTION_TITLES],
    )
    parser_add.add_argument(
        "-i",
        "--input",
        default=None,
        help="Change notes, can be provided as a pipe-in as well.",
    )
    parser_add.add_argument(
        "--created",
        default="",
        help="Created date in `YYYY-MM-DD` format.",
    )
    parser_add.add_argument(
        "-p",
        "--changelog-path",
        type=Path,
        default=Path.cwd() / "CHANGELOG.md",
        help="Full path to changelog file. Default: ./CHANGELOG.md",
    )

    parser_set = subparsers.add_parser("set", help="Write new or existing record to CHANGELOG.md")
    parser_set.add_argument(
        "name",
        type=get_version_latest_or_unreleased,
        default=LATEST,
        help="Release name: version, `latest` or `unreleased`",
    )
    parser_set.add_argument(
        "section",
        help="Section name or `All`",
        nargs="?",
        type=lambda x: x.lower(),
        default=SECTION_ALL,
        choices=[SECTION_ALL, *SECTION_TITLES],
    )
    parser_set.add_argument(
        "-i",
        "--input",
        default=None,
        help="Change notes, can be provided as a pipe-in as well.",
    )
    parser_set.add_argument(
        "--created",
        default="",
        help="Created date in `YYYY-MM-DD` format.",
    )
    parser_set.add_argument(
        "-p",
        "--changelog-path",
        type=Path,
        default=Path.cwd() / "CHANGELOG.md",
        help="Full path to changelog file. Default: ./CHANGELOG.md",
    )

    parser_get = subparsers.add_parser("get", help="Get changelog record")
    parser_get.add_argument(
        "name",
        nargs="?",
        type=get_version_latest_or_unreleased,
        default=LATEST,
        help="Release name: version, `latest` or `unreleased`",
    )
    parser_get.add_argument(
        "section",
        help="Section name or `All`",
        nargs="?",
        type=lambda x: x.lower(),
        default=SECTION_ALL,
        choices=[SECTION_ALL, *SECTION_TITLES],
    )
    parser_get.add_argument(
        "-p",
        "--changelog-path",
        type=get_existing_path,
        default=Path.cwd() / "CHANGELOG.md",
        help="Full path to changelog file. Default: ./CHANGELOG.md",
    )

    parser_format = subparsers.add_parser("format", help="Format release notes")
    parser_format.add_argument(
        "-i",
        "--input",
        default=None,
        help="Change notes, can be provided as a pipe-in as well.",
    )

    parser_list = subparsers.add_parser("list", help="List versions")
    parser_list.add_argument(
        "-p",
        "--changelog-path",
        type=get_existing_path,
        default=Path.cwd() / "CHANGELOG.md",
        help="Full path to changelog file. Default: ./CHANGELOG.md",
    )

    parser_version = subparsers.add_parser(
        "version", help="Bump version according to release notes"
    )
    parser_version.add_argument(
        "version",
        type=Version,
        help="Release version",
    )
    parser_version.add_argument(
        "-i",
        "--input",
        default=None,
        help="Change notes, can be provided as a pipe-in as well.",
    )

    result = parser.parse_args(args)

    if hasattr(result, "input") and result.input is None:
        result.input = get_stdin()

    if result.command == "get" and not result.changelog_path.exists():
        raise argparse.ArgumentTypeError(
            "CHANGELOG.md does not exist in current folder, run `logchange init`"
        )

    return result
