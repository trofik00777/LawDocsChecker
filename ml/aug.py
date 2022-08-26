from annoy import AnnoyIndex
from navec import Navec
import json


class Augmentator(object):
    def __init__(self):
        self.model = AnnoyIndex(300, "euclidean")
        self.model.load("synonims.ann")
        self.navec = Navec.load("navec_hudlit_v1_12B_500K_300d_100q.tar")
        with open("words.json") as f:
            self.words = json.load(f)

    def find_close_word(self, word):
        if word not in self.navec:
            return word
        close_word_id = self.model.get_nns_by_vector(self.navec[word], 2)[1]
        return self.words[close_word_id]


a = Augmentator()
print(a.find_close_word("россия"))
print(a.find_close_word("зеленский"))
print(a.find_close_word("слово"))
