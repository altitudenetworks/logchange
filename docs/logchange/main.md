# Main

> Auto-generated documentation for [logchange.main](https://github.com/vemel/logchange/blob/main/logchange/main.py) module.

- [logchange](../README.md#logchange---changelog-manager) / [Modules](../MODULES.md#logchange-modules) / [Logchange](index.md#logchange) / Main
    - [CLIError](#clierror)
    - [main_api](#main_api)
    - [main_cli](#main_cli)
    - [setup_logging](#setup_logging)

## CLIError

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/main.py#L17)

```python
class CLIError(Exception):
```

Main CLI error

## main_api

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/main.py#L23)

```python
def main_api(config: argparse.Namespace) -> str:
```

Main API entrypoint.

## main_cli

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/main.py#L34)

```python
def main_cli() -> None:
```

Main entrypoint for CLI.

## setup_logging

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/main.py#L9)

```python
def setup_logging(level: int) -> None:
```
