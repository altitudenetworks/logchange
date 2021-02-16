# Cli Parser

> Auto-generated documentation for [logchange.cli_parser](https://github.com/vemel/logchange/blob/main/logchange/cli_parser.py) module.

Main CLI parser.

- [logchange](../README.md#logchange---changelog-manager) / [Modules](../MODULES.md#logchange-modules) / [Logchange](index.md#logchange) / Cli Parser
    - [get_existing_path](#get_existing_path)
    - [get_stdin](#get_stdin)
    - [get_version_latest_or_unreleased](#get_version_latest_or_unreleased)
    - [parse_args](#parse_args)

## get_existing_path

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/cli_parser.py#L15)

```python
def get_existing_path(value: str) -> Path:
```

## get_stdin

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/cli_parser.py#L36)

```python
def get_stdin() -> str:
```

Get input from stdin.

#### Returns

Parsed version.

## get_version_latest_or_unreleased

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/cli_parser.py#L22)

```python
def get_version_latest_or_unreleased(value: str) -> str:
```

## parse_args

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/cli_parser.py#L49)

```python
def parse_args(args: Sequence[str]) -> argparse.Namespace:
```

Main CLI parser.

#### Returns

Argument parser Namespace.
