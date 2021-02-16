# RecordSection

> Auto-generated documentation for [logchange.record_section](https://github.com/vemel/logchange/blob/main/logchange/record_section.py) module.

- [logchange](../README.md#logchange---changelog-manager) / [Modules](../MODULES.md#logchange-modules) / [Logchange](index.md#logchange) / RecordSection
    - [RecordSection](#recordsection)
        - [RecordSection().append](#recordsectionappend)
        - [RecordSection().append_lines](#recordsectionappend_lines)
        - [RecordSection().is_empty](#recordsectionis_empty)
        - [RecordSection().name](#recordsectionname)
        - [RecordSection().render](#recordsectionrender)

## RecordSection

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_section.py#L6)

```python
class RecordSection():
    def __init__(title: str, body: str) -> None:
```

### RecordSection().append

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_section.py#L21)

```python
def append(appendix: str) -> None:
```

### RecordSection().append_lines

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_section.py#L24)

```python
def append_lines(body: str) -> None:
```

### RecordSection().is_empty

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_section.py#L15)

```python
def is_empty() -> bool:
```

### RecordSection().name

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_section.py#L11)

```python
@property
def name() -> str:
```

### RecordSection().render

[[find in source code]](https://github.com/vemel/logchange/blob/main/logchange/record_section.py#L18)

```python
def render() -> str:
```
