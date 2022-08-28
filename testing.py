import csv

from ml.data_preprocessing import DocProcessor
from ml.models import BaseModel
import docx


def run(filename: str, answ):
    try:
        file = docx.Document(filename)
    except Exception as e:
        print(f"Oops! {e}")
        return


    model = BaseModel()
    parts = DocProcessor.preprocess_doc_splitted_by_brackets(file)
    num = 1
    file_id = filename.split('/')[-1].rstrip(".docx")
    for text, flag in parts:
        if flag:
            label = model(text) + 1
            print(f"{file_id}\t-\t{num}\t-\t{label}\t-\t'{text}'")
            answ.append([file_id, num, label])

            num += 1


def main(dir: str):
    answ = []
    for i in range(1, 11):
        run(f"{dir}/{i}.docx", answ)

    with open(f"{dir}/answerv40.csv", "wt", encoding='utf-8') as fp:
        writer = csv.writer(fp, delimiter=";")
        writer.writerow(["file_id", "id", "class"])  # write header
        writer.writerows(answ)


if __name__ == "__main__":
    main("path/to/directory")
