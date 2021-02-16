# ChangeLog

> Auto-generated documentation for [logchange.changelog](https://github.com/vemel/logchange/blob/main/logchange/changelog.py) module.

- [logchange](../README.md#logchange---changelog-manager) / [Modules](../MODULES.md#logchange-modules) / [Logchange](index.md#logchange) / ChangeLog
    - [ChangeLog](#changelog)
        - [ChangeLog().add_release](#changelogadd_release)
        - [ChangeLog().format_released](#changelogformat_released)
        - [ChangeLog().get_latest](#changelogget_latest)
        - [ChangeLog().get_record](#changelogget_record)
        - [ChangeLog().get_unreleased](#changelogget_unreleased)
        - [ChangeLog().iterate_records](#changelogiterate_records)
        - [ChangeLog.parse](#changelogparse)
        - [ChangeLog().released](#changelogreleased)
        - [ChangeLog().render](#changelogrender)
        - [ChangeLog().update_release](#changelogupdate_release)

## ChangeLog

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/changelog.py#L12)

```python
class ChangeLog():
    def __init__(head: str, released: str, unreleased: str) -> None:
```

#### Attributes

- `RELEASED_MARKER` - Released section title in CHANGELOG.md: `'## ['`
- `UNRELEASED_MARKER` - Unreleased section title in CHANGELOG.md: `'## [Unreleased]'`

### ChangeLog().add_release

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/changelog.py#L100)

```python
def add_release(record: Record) -> None:
```

#### See also

- [Record](record.md#record)

### ChangeLog().format_released

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/changelog.py#L93)

```python
def format_released() -> None:
```

### ChangeLog().get_latest

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/changelog.py#L70)

```python
def get_latest() -> Optional[Record]:
```

### ChangeLog().get_record

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/changelog.py#L79)

```python
def get_record(version: Version) -> Optional[Record]:
```

### ChangeLog().get_unreleased

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/changelog.py#L76)

```python
def get_unreleased() -> Record:
```

#### See also

- [Record](record.md#record)

### ChangeLog().iterate_records

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/changelog.py#L86)

```python
def iterate_records() -> Iterator[Record]:
```

### ChangeLog.parse

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/changelog.py#L34)

```python
@classmethod
def parse(text: str) -> _R:
```

### ChangeLog().released

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/changelog.py#L27)

```python
@property
def released() -> List[Record]:
```

### ChangeLog().render

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/changelog.py#L62)

```python
def render() -> str:
```

### ChangeLog().update_release

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/changelog.py#L107)

```python
def update_release(record: Record) -> None:
```

#### See also

- [Record](record.md#record)
