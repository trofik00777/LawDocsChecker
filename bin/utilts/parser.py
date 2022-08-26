from operator import index
import os
import docx
import re
import csv


data = []  # text, filename, class, is_normal(0/1)
has = []  # filename, classes(0/1)...
for filename in os.listdir("./helper/docs"):
    print(filename)
    doc = docx.Document("./helper/docs/" + filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    text = ''.join(fullText)
    # print(text)
    class_left = None
    class_right = None
    ind_l = ind_r = None
    chet = 0
    cl = set()
    for i in range(len(text)):
        if text[i] == "{":
            try:
                last_i = i + text[i:i + 5].index("}")
            except:
                print(text[i:i + 10])
                exit(0)

            if chet % 2 == 0:
                class_left = int(text[i + 1:last_i])
                ind_l = last_i + 1
            else:
                class_right = int(text[i + 1:last_i])
                ind_r = i
                cl.add(class_left)
                cl.add(class_right)
                if class_left == class_right:
                    data.append([text[ind_l:ind_r], filename, class_left, 1])
                else:
                    print("WARNING: " + str(i) + " - " + filename + " - " + str(class_left) + "/" + str(class_right))
                    data.append([text[ind_l:ind_r], filename, class_left, 0])
                    data.append([text[ind_l:ind_r], filename, class_right, 0])
            
            chet += 1
    
    toadd = [filename]    
    has.append([
        filename
    ] + [int(i in cl)
        for i in range(1, 40)
    ])


    # for ind in range(1, 40):
    #     indexes = [i + 2 + len(str(ind)) for i in range(len(text)) if text[i:i + 2 + len(str(ind))] == "{" + str(ind) + "}"]
    #     print(ind, indexes)
    #     if len(indexes) > 0:
    #         print(text[indexes[0]:indexes[1]])
    #     for curr in range(0, len(indexes), 2):
    #         data.append([text[indexes[curr]:indexes[curr + 1]], filename, ind])

    # break


# with open("dataset.csv", "wt", encoding='utf-8') as fp:
#     writer = csv.writer(fp, delimiter=",")
#     writer.writerow(["text", "filename", "class", "data_is_ok"])  # write header
#     writer.writerows(data)

with open("classes.csv", "wt", encoding='utf-8') as fp:
    writer = csv.writer(fp, delimiter=",")
    writer.writerow(["filename"] + [i for i in range(1, 40)])  # write header
    writer.writerows(has)
