# Executor

> Auto-generated documentation for [logchange.executor](https://github.com/vemel/logchange/blob/main/logchange/executor.py) module.

CLI commands executor.

- [logchange](../README.md#logchange---changelog-manager) / [Modules](../MODULES.md#logchange-modules) / [Logchange](index.md#logchange) / Executor
    - [Executor](#executor)
        - [Executor().changelog](#executorchangelog)
        - [Executor().changelog_path](#executorchangelog_path)
        - [Executor().execute](#executorexecute)
        - [Executor().get_today](#executorget_today)
        - [Executor().input](#executorinput)
        - [Executor().release_name](#executorrelease_name)
        - [Executor().save_changelog](#executorsave_changelog)
    - [ExecutorError](#executorerror)

## Executor

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/executor.py#L25)

```python
class Executor():
    def __init__(config: argparse.Namespace) -> None:
```

CLI commands executor.

### Executor().changelog

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/executor.py#L47)

```python
@property
def changelog() -> ChangeLog:
```

#### See also

- [ChangeLog](changelog.md#changelog)

### Executor().changelog_path

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/executor.py#L40)

```python
@property
def changelog_path() -> Path:
```

### Executor().execute

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/executor.py#L85)

```python
def execute() -> str:
```

Execute command based on `config`.

#### Returns

String output.

### Executor().get_today

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/executor.py#L44)

```python
def get_today() -> str:
```

### Executor().input

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/executor.py#L35)

```python
@property
def input() -> str:
```

### Executor().release_name

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/executor.py#L62)

```python
@property
def release_name() -> str:
```

### Executor().save_changelog

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/executor.py#L59)

```python
def save_changelog(changelog: ChangeLog) -> None:
```

#### See also

- [ChangeLog](changelog.md#changelog)

## ExecutorError

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/executor.py#L19)

```python
class ExecutorError(Exception):
```

Main CLI commands executor error.
