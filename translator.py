from owlmixin import OwlMixin

from clients.client import TranslationClient


class TranslationResult(OwlMixin):
    english: str
    chinese_from_english: str
    japanese_from_chinese: str
    english_from_chinese: str


def bulk_translate(english: str, client: TranslationClient) -> TranslationResult:
    chinese = client.translate(english, from_lang="en", to_lang="zh")
    return TranslationResult.from_dict(
        {
            "english": english,
            "chinese_from_english": chinese,
            "japanese_from_chinese": client.translate(
                chinese, from_lang="zh", to_lang="ja"
            ),
            "english_from_chinese": client.translate(
                chinese,
                from_lang="zh",
                to_lang="en-US",
            ),
        }
    )
