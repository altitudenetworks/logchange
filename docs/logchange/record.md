# Record

> Auto-generated documentation for [logchange.record](https://github.com/vemel/logchange/blob/main/logchange/record.py) module.

- [logchange](../README.md#logchange---changelog-manager) / [Modules](../MODULES.md#logchange-modules) / [Logchange](index.md#logchange) / Record
    - [Record](#record)
        - [Record().append_section](#recordappend_section)
        - [Record().is_empty](#recordis_empty)
        - [Record().merge_body](#recordmerge_body)
        - [Record().name](#recordname)
        - [Record.parse](#recordparse)
        - [Record().render](#recordrender)
        - [Record().set_body](#recordset_body)
        - [Record().set_section](#recordset_section)

## Record

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record.py#L12)

```python
class Record():
    def __init__(version: Version, body: RecordBody, created: str):
```

#### See also

- [RecordBody](record_body.md#recordbody)

### Record().append_section

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record.py#L92)

```python
def append_section(title: str, body: str) -> None:
```

### Record().is_empty

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record.py#L75)

```python
def is_empty() -> bool:
```

### Record().merge_body

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record.py#L107)

```python
def merge_body(text: str) -> None:
```

### Record().name

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record.py#L26)

```python
@property
def name() -> str:
```

### Record.parse

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record.py#L56)

```python
@classmethod
def parse(text: str) -> _R:
```

### Record().render

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record.py#L42)

```python
def render() -> str:
```

### Record().set_body

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record.py#L102)

```python
def set_body(text: str) -> None:
```

### Record().set_section

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record.py#L78)

```python
def set_section(title: str, body: str) -> None:
```
