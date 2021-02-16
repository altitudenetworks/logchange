# RecordBody

> Auto-generated documentation for [logchange.record_body](https://github.com/vemel/logchange/blob/main/logchange/record_body.py) module.

- [logchange](../README.md#logchange---changelog-manager) / [Modules](../MODULES.md#logchange-modules) / [Logchange](index.md#logchange) / RecordBody
    - [RecordBody](#recordbody)
        - [RecordBody().append_lines](#recordbodyappend_lines)
        - [RecordBody().append_to_all](#recordbodyappend_to_all)
        - [RecordBody().bump_version](#recordbodybump_version)
        - [RecordBody().get_section](#recordbodyget_section)
        - [RecordBody().is_empty](#recordbodyis_empty)
        - [RecordBody().merge](#recordbodymerge)
        - [RecordBody.parse](#recordbodyparse)
        - [RecordBody().render](#recordbodyrender)
        - [RecordBody().set_section](#recordbodyset_section)

## RecordBody

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_body.py#L12)

```python
class RecordBody():
    def __init__(sections: Iterable[RecordSection] = ()) -> None:
```

### RecordBody().append_lines

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_body.py#L51)

```python
def append_lines(title: str, body: str) -> None:
```

### RecordBody().append_to_all

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_body.py#L54)

```python
def append_to_all(appendix: str) -> None:
```

### RecordBody().bump_version

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_body.py#L20)

```python
def bump_version(old_version: Version) -> Version:
```

### RecordBody().get_section

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_body.py#L33)

```python
def get_section(title: str) -> RecordSection:
```

#### See also

- [RecordSection](record_section.md#recordsection)

### RecordBody().is_empty

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_body.py#L97)

```python
def is_empty() -> bool:
```

### RecordBody().merge

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_body.py#L59)

```python
def merge(other: _R) -> _R:
```

### RecordBody.parse

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_body.py#L69)

```python
@classmethod
def parse(text: str) -> _R:
```

### RecordBody().render

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_body.py#L36)

```python
def render() -> str:
```

### RecordBody().set_section

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_body.py#L47)

```python
def set_section(title: str, body: str) -> None:
```
