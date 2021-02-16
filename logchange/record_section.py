from typing import TypeVar

_R = TypeVar("_R", bound="RecordSection")


class RecordSection:
    def __init__(self, title: str, body: str) -> None:
        self.title = title
        self.body = body

    @property
    def name(self) -> str:
        return self.title.capitalize()

    def is_empty(self) -> bool:
        return self.body == ""

    def render(self) -> str:
        return f"### {self.name}\n{self.body}"

    def append(self, appendix: str) -> None:
        self.body = f"{self.body}{appendix}"

    def append_lines(self, body: str) -> None:
        if not self.body:
            self.body = body
            return

        parts = [self.body, body]
        parts = [i for i in parts if i]
        self.body = "\n".join(parts)
