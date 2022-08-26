import spacy


class Preprocessor(object):
    def __init__(self):
        self.nlp = spacy.load("ru_core_news_lg")

    def light_preprocess(self, text):
        pass

    def hard_preprocess(self, text):
        pass