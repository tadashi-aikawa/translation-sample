import os

import fire
from owlmixin import OwlMixin, TList
import translator
from clients import factory


class Config(OwlMixin):
    # OwlMixin doesn't support Literal types
    services: TList[str]


class InputRecord(OwlMixin):
    english: str
    memo: str


FIELDS = [
    "english",
    "chinese_from_english",
    "japanese_from_chinese",
    "english_from_chinese",
]


def execute(input="input.csv", config="config.yaml", output_dir="output"):
    cfg: Config = Config.from_yamlf(config)
    records: TList[InputRecord] = InputRecord.from_csvf_to_list(
        input, ["english", "memo"]
    )

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    for service in cfg.services:
        translation_client = factory.create(service)
        result = records.map(
            lambda r: translator.bulk_translate(r.english, translation_client)
        )

        result.to_jsonf(f"{output_dir}/{service}.json", indent=4)
        result.to_csvf(
            f"{output_dir}/{service}.csv", tsv=True, with_header=True, fieldnames=FIELDS
        )


if __name__ == "__main__":
    fire.Fire(execute)
