import spacy
from functools import lru_cache

# pip install spacy==3.1.0
# python -m spacy download ru_core_news_lg


class Preprocessor(object):
    def __init__(self):
        self.nlp = spacy.load("ru_core_news_lg")

    def light_preprocess(self, text):
        pass

    @lru_cache(10**10)
    def lemmatizate(self, word):
        return self.nlp(word)[0].lemma_

    def hard_preprocess(self, text):
        """Только кириллица, слова лемматизированы, все числа заменены токеном <num>, без стоп слов"""
        pass


p = Preprocessor()
print(p.lemmatizate("ноутбуком"))