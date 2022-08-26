from annoy import AnnoyIndex
from navec import Navec
import json
from transformers import T5ForConditionalGeneration, T5Tokenizer
from random import choice
import os


os.environ["SYNONIMS"] = "../../checkpoints/synonims.ann"
os.environ["EMBEDDINGS"] = "../../checkpoints/navec_hudlit_v1_12B_500K_300d_100q.tar"
os.environ["WORDS"] = "../../checkpoints/words.json"


class Augmentator(object):
    """Объект для расширения числа данных через замены слова на синонимы, перемешивание слов, удаления слов,
    добавления слов, обратный перевод """

    def __init__(self):
        self.model = AnnoyIndex(300, "euclidean")
        self.model.load(os.environ["SYNONIMS"])
        self.navec = Navec.load(os.environ["EMBEDDINGS"])
        with open(os.environ["WORDS"]) as f:
            self.words = json.load(f)
        self.model = T5ForConditionalGeneration.from_pretrained('cointegrated/rut5-base-paraphraser')
        self.tokenizer = T5Tokenizer.from_pretrained('cointegrated/rut5-base-paraphraser')
        self.model.cpu()
        self.model.eval()

    def find_close_word(self, word: str) -> str:
        """Находит для слова синоним через annoy поиска ближайшего эмбеддинга в Natasha"""
        if word not in self.navec:
            return word
        close_words_id = self.model.get_nns_by_vector(self.navec[word], 5)[1:5]
        return self.words[choice(close_words_id)]

    def deep_augment(self, text: str, beams=5, grams=4, do_sample=False) -> str:
        """Нейросетевая аугментация"""
        x = self.tokenizer(text, return_tensors='pt', padding=True).to(self.model.device)
        max_size = int(x.input_ids.shape[1] * 1.5 + 10)
        out = self.model.generate(**x, encoder_no_repeat_ngram_size=grams, num_beams=beams, max_length=max_size,
                                  do_sample=do_sample)
        return self.tokenizer.decode(out[0], skip_special_tokens=True)

    def augment(self, text: str) -> str:
        """Кастомная аугментация"""
        text = text.split()
        for i in range(len(text)):
            if choice(range(2)) == 0:
                text[i] = self.find_close_word(text[i])
            if i > 0 and choice(range(5)) == 0:
                text[i - 1], text[i] = text[i], text[i - 1]
            if choice(range(15)) == 0:
                text[i] = ""
            if choice(range(10)) == 0:
                text[i] = text[i] + " и " + self.find_close_word(text[i])
        return " ".join(text)
