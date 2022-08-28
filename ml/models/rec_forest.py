import pickle


class RecForest(object):
    def __init__(self):
        with open("../../checkpoints/rec_forest.pkl", "rb") as f:
            self.model = pickle.load(f)

    def hard_requirements(self, x):
        """
            Принимает номера классов в документе, возвращает словарь вида
            Причина: массив классов, которых не хватает
            """
        result = {}
        for cls in x:
            if cls == 2 and not (27 in x):
                result['Cубсидия предоставляется в целях реализации такого проекта, программы'] = [27]
            if cls == 23 and not (6 in x):
                result['Получатель субсидии определяется по результатам отбора'] = [6]
            if cls == 26 and not (38 in x):
                result[
                    'Субсидия предоставляется на развитие инновационной деятельности предусматривают последующее предоставление средств иным лицам, в соответствии с главой IV.1 Федерального закона «О науке и государственной научно-технической политике»'] = [
                    38]
            if (cls == 31 or cls == 32) and (30 in x):
                result['Субсидия предоставляется на финансовое обеспечение затрат'] = [30]
            if (cls == 33 or cls == 34 or cls == 4):
                temp = [10]
                if not (33 in x):
                    temp.append(33)
                if not (34 in x):
                    temp.append(34)
                if not (4 in x):
                    temp.append(4)
                result[
                    'Предусматривается либо в порядке финансового обеспечения затрат либо возмещения затрат (недополученных доходов)'] = temp
        return result

    def __call__(self, x) -> int:
        assert len(x) == 39
        result = self.hard_requirements(x)
        if len(result.keys()) > 0:
            return 0
        return self.model.predict([[i for i in x]])[0]


if __name__ == "__main__":
    m = RecForest()
    print(m([0 for i in range(39)]))
