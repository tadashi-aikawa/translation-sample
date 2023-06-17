import os
from typing import Literal

from clients.client import TranslationClient
from clients.deepl_client import DeepLClient

Service = Literal["deepl"]


def create(service: Service) -> TranslationClient:
    match service:
        case "deepl":
            return DeepLClient(os.environ.get("DEEPL_TOKEN"))
        case _:
            raise AssertionError(f"引数serviceに {service} は指定できません")
