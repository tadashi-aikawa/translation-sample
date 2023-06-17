import deepl

from clients.client import TranslationClient, Language


class DeepLClient(TranslationClient):
    translator: deepl.Translator

    def __init__(self, token: str):
        self.translator = deepl.Translator(token)

    def translate(self, english: str, *, from_lang: Language, to_lang: Language) -> str:
        return self.translator.translate_text(
            english, target_lang=to_lang, source_lang=from_lang
        ).text
