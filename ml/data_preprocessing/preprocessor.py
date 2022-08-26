import spacy
from functools import lru_cache
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import csv


# pip install spacy==3.1.0
# python -m spacy download ru_core_news_lg
# nltk.download("stopwords")
# nltk.download('punkt')


class Preprocessor(object):
    def __init__(self):
        self.nlp = spacy.load("ru_core_news_lg")
        self.alphabet = set("йцукенгшщзхъфывапролджэёячсмитьбю")
        self.stops = set(stopwords.words('russian')).union(self.alphabet)

    def light_preprocess(self, text):
        pass

    @lru_cache(10 ** 10)
    def lemmatizate(self, word):
        return self.nlp(word)[0].lemma_

    def hard_preprocess(self, text: str, is_logging=False):
        """Только кириллица, слова лемматизированы, все числа заменены токеном <num>, без стоп слов"""
        tokens = word_tokenize(
            re.sub(r'[^\w\s]', ' ', text.lower())
        )
        nice_words = []
        for token in tokens:
            lem_tok = self.lemmatizate(token)

            if lem_tok in self.stops:
                if is_logging:
                    print(lem_tok)
                continue

            for ch in lem_tok:
                if ch.isdigit():
                    nice_words.append("<num>")
                    break
                if ch not in self.alphabet:
                    break
            else:
                nice_words.append(lem_tok)

        return nice_words


if __name__ == "__main__":
    p = Preprocessor()
    print(p.lemmatizate("ноутбуком"))
    with open("../data/dataset.csv", encoding='utf-8') as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        next(reader, None)  # skip the headers
        data_read = [row for row in reader]

        data_write = []
        for row in data_read:
            data_write.append([' '.join(p.hard_preprocess(row[0]))] + row[1:])

    with open("../data/preprocess_dataset.csv", "wt", encoding='utf-8') as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(["text", "filename", "class", "data_is_okay"])  # write header
        writer.writerows(data_write)
