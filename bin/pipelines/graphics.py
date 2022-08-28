import matplotlib.pyplot as plt
import json


with open("metrics.json") as f:
    metrics = json.load(f)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(metrics["train_loss"])

plt.subplot(1, 2, 2)
plt.plot(metrics["test_acc"], label="acc")
plt.plot(metrics["test_precision"], label="precision")
plt.plot(metrics["test_recall"], label="recall")
plt.legend()
plt.show()
