from transformers import AutoTokenizer
import torch


class BaseModel(object):
    def __init__(self, *kwargs):
        self.tokenizer = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny")
        self.max_len = 512
        if torch.cuda.is_available():
            device = "cuda"
        else:
            device = "cpu"
        self.model = torch.load("../../checkpoints/bert_v10.pt", map_location=torch.device(device))
        self.model = self.model.eval()
        self.device = torch.device(device)

    def __call__(self, text: str) -> int:
        encoding = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=self.max_len,
            return_token_type_ids=False,
            padding='max_length',
            return_attention_mask=True,
            return_tensors='pt',
        )
        inp = {"input_ids": encoding['input_ids'].flatten().view(1, self.max_len),
               "attention_mask": encoding['attention_mask'].flatten().view(1, self.max_len)}
        input_ids = inp["input_ids"].to(self.device)
        attention_mask = inp["attention_mask"].to(self.device)
        y_pred = self.model(input_ids=input_ids, attention_mask=attention_mask).logits.argmax(1).tolist()
        return y_pred[0]


if __name__ == "__main__":
    m = BaseModel()
    print(m("кто прочитал тот пидор"))
