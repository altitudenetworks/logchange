class EOLFixer:
    WINDOWS_LINE_ENDING = "\r\n"
    UNIX_LINE_ENDING = "\n"

    @classmethod
    def is_windows(cls, text: str) -> bool:
        return cls.WINDOWS_LINE_ENDING in text

    @classmethod
    def to_unix(cls, text: str) -> str:
        if not cls.is_windows(text):
            return text

        return text.replace(cls.WINDOWS_LINE_ENDING, cls.UNIX_LINE_ENDING)

    @classmethod
    def to_windows(cls, text: str) -> str:
        if cls.is_windows(text):
            return text

        return text.replace(cls.UNIX_LINE_ENDING, cls.WINDOWS_LINE_ENDING)
