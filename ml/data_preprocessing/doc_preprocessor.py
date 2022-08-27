import re
from string import punctuation
from typing import List

from loguru import logger

from docx import Document

import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

russian_stopwords = stopwords.words("russian")

patterns = re.compile(r"[A-Za-z0-9!#$%&'()*+,./:;<=>?@[\]^_`{|}~—\"\-]+")
split_regex = re.compile(r'[.|!|?|…]')

COUNT_POSSIBLE_CHARS_BETWEEN_BRACKETS = 2


class DocProcessor:
    @staticmethod
    def get_full_text(doc: Document):
        full_text = []

        for para in doc.paragraphs:
            full_text.append(para.text)

        return '\n'.join(full_text)

    @classmethod
    def preprocess_doc_splitted_by_sentences(cls, doc: Document) -> List[str]:
        sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(cls.get_full_text(doc))])
        sentences = list(map(cls._preprocess_text, sentences))
        sentences = list(filter(lambda elem: not (elem is None), sentences))
        return sentences

    @classmethod
    def preprocess_doc_splitted_by_brackets(cls, doc: Document) -> List[tuple[str, bool]]:
        text = cls.get_full_text(doc)
        logger.debug(text)
        is_right = False
        left_bracket = right_bracket = 0
        paragraphs = []
        for i in range(len(text)):
            if text[i] == "{":
                last_i = i
                try:
                    last_i = i + text[i:i + COUNT_POSSIBLE_CHARS_BETWEEN_BRACKETS + 2].index("}")
                except Exception as e:
                    logger.error(f"There are no bracket at '{text[i:i + 10]}'")

                if is_right:
                    right_bracket = i
                    paragraphs.append((text[left_bracket + 1:right_bracket], True))
                else:
                    left_bracket = last_i
                    paragraphs.append((text[right_bracket + 1:left_bracket], False))
                is_right = not is_right
        return paragraphs

    @staticmethod
    def _preprocess_text(text: str) -> str:
        text = re.sub(patterns, ' ', text)
        tokens = text.lower().split()
        f_tokens = []

        for token in tokens:
            if all([token not in russian_stopwords,
                    token != " ",
                    token.strip() not in punctuation,
                    ]):
                f_tokens.append(token)
        text = " ".join(tokens)
        if len(tokens) > 2:
            return text


if __name__ == "__main__":
    file = Document("/Users/trofik00777/Documents/parser/helper/docs/Postanovlenie_Pravitelstva_Rossiyskoy_Federatsii_ot_04_03_2021__314.docx")
    print(DocProcessor.preprocess_doc_splitted_by_brackets(file))
