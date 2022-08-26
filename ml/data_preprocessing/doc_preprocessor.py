import re
from string import punctuation
from typing import List

from docx import Document

import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

russian_stopwords = stopwords.words("russian")

patterns = re.compile(r"[A-Za-z0-9!#$%&'()*+,./:;<=>?@[\]^_`{|}~—\"\-]+")
split_regex = re.compile(r'[.|!|?|…]')


class DocProcessor:
    @classmethod
    def preprocess_doc(cls, doc: Document) -> List[str]:
        full_text = []

        for para in doc.paragraphs:
            full_text.append(para.text)

        text = ''.join(full_text)
        sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(text)])
        sentences = list(map(cls._preprocess_text, sentences))
        sentences = list(filter(lambda elem: not (elem is None), sentences))
        return sentences

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
