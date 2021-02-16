import argparse
import logging
import sys

from logchange.cli_parser import parse_args
from logchange.executor import Executor, ExecutorError


def setup_logging(level: int) -> None:
    logger = logging.getLogger("logchange")
    logger.setLevel(level)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
    logger.addHandler(stream_handler)


class CLIError(Exception):
    """
    Main CLI error
    """


def main_api(config: argparse.Namespace) -> str:
    """
    Main API entrypoint.
    """
    executor = Executor(config)
    try:
        return executor.execute()
    except ExecutorError as e:
        raise CLIError(e)


def main_cli() -> None:
    """
    Main entrypoint for CLI.
    """
    config = parse_args(sys.argv[1:])
    setup_logging(logging.INFO)
    try:
        output = main_api(config)
    except CLIError as e:
        sys.stderr.write(f"ERROR {e}\n")
        sys.exit(1)

    if output:
        sys.stdout.write(f"{output}\n")
