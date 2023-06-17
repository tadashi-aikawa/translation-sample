from typing import Literal

Language = Literal["en", "en-US", "ja", "zh"]


class TranslationClient:
    def translate(self, english: str, *, from_lang: Language, to_lang: Language) -> str:
        raise NotImplementedError()
