import textwrap
from pathlib import Path


def strip_empty_lines(text: str) -> str:
    lines = text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)

    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def dedent(text: str) -> str:
    return textwrap.dedent(strip_empty_lines(text))


def print_path(path: Path) -> str:
    if path.is_absolute():
        cwd = Path.cwd()
        if path == cwd or path.parts <= cwd.parts:
            return str(path)

        try:
            path = path.relative_to(cwd)
        except ValueError:
            return str(path)

    if len(path.parts) == 1:
        return f"./{path}"

    return str(path)
