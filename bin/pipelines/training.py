import os
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score, accuracy_score
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer, BertForSequenceClassification
import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
import json

BATCH_SIZE = 32
EPOCHS = 40
LR = 0.001
LOG_INTERVAL = 500

torch.cuda.empty_cache()
if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"
device = torch.device(device)


class CustomDataset(Dataset):
    def __init__(self, texts, targets, tokenizer, max_len=512):
        self.texts = list(texts)
        self.targets = [int(i) - 1 for i in list(targets)]
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        text = str(self.texts[index])
        target = self.targets[index]

        encoding = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=self.max_len,
            return_token_type_ids=False,
            padding='max_length',
            return_attention_mask=True,
            return_tensors='pt',
        )

        return {
            'text': text,
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'targets': torch.tensor(target, dtype=torch.long)
        }


df = pd.read_csv("../../ml/data/augmented_dataset.csv").dropna()[["text", "class"]]

tokenizer = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny")
model = BertForSequenceClassification.from_pretrained("cointegrated/rubert-tiny").to(device)
model.classifier = nn.Linear(312, 64).to(device)
train, test = train_test_split(df, train_size=0.8)
train = CustomDataset(train["text"], train["class"], tokenizer)
test = CustomDataset(test["text"], test["class"], tokenizer)
train_dataloader = DataLoader(train, batch_size=BATCH_SIZE, shuffle=False, num_workers=12)
test_dataloader = DataLoader(test, batch_size=BATCH_SIZE, shuffle=False, num_workers=12)

optimizer = torch.optim.Adam(model.parameters(), lr=LR)
criterion = nn.CrossEntropyLoss()


device = torch.device(device)
k = len(train) // BATCH_SIZE
metrics = {"train_loss": [], "test_acc": [], "test_precision": [], "test_recall": []}
for epoch in range(1, EPOCHS + 1):
    losses = []
    model = model.train()
    for ind, data in enumerate(train_dataloader):
        input_ids = data["input_ids"].to(device)
        attention_mask = data["attention_mask"].to(device)
        targets = data["targets"]
        y_pred = model(input_ids=input_ids, attention_mask=attention_mask)
        loss = criterion(y_pred.logits.cpu(), targets)
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()
        optimizer.zero_grad()
        losses.append(loss.tolist())
        if ind % LOG_INTERVAL == 0:
            print(f"{ind}/{k} loss: {loss}")
    metrics["train_loss"].append(sum(losses) / len(losses))
    torch.save(model, "../../checkpoints/bert_v" + str(epoch) + ".pt")
    model = model.eval()
    predictions = []
    values = []
    for ind, data in tqdm(enumerate(test_dataloader)):
        input_ids = data["input_ids"].to(device)
        attention_mask = data["attention_mask"].to(device)
        targets = data["targets"].tolist()
        y_pred = model(input_ids=input_ids, attention_mask=attention_mask).logits.argmax(1).tolist()
        values.extend(targets)
        predictions.extend(y_pred)
    acc = accuracy_score(values, predictions)
    precision = precision_score(values, predictions, average="micro")
    recall = recall_score(values, predictions, average="micro")
    metrics["test_acc"].append(acc)
    metrics["test_recall"].append(recall)
    metrics["test_precision"].append(precision)
    print(f"Test acc {acc} ; Test precision {precision} ; Test recall {recall})")
with open("metrics.json", "w") as f:
    json.dump(metrics, f)
