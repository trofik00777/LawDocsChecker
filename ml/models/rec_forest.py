import pickle


class RecForest(object):
    def __init__(self):
        with open("../../checkpoints/rec_forest.pkl", "rb") as f:
            self.model = pickle.load(f)

    def __call__(self, x) -> int:
        assert len(x) == 39
        return self.model.predict([[i for i in x]])[0]


if __name__ == "__main__":
    m = RecForest()
    print(m([0 for i in range(39)]))
