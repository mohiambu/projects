import random
from collections import defaultdict

def dataread(path):
    with open(path,"r",encoding= "utf-8") as file:
        data = file.read()

    P = data.split("\n\n")
    return P



path = "C://Users//M7MDA//Downloads//Project2_dataset_similarity.txt"
d = dataread(path)


def shingles(text,k = 5):
    text = text.strip().split()
    shingles = []
    for i in range(len(text)-k+1):
        s = text[i:i+k]
        c = " ".join(s)
        shingles.append(c)
    return shingles


def Jiccard(s1,s2):
    setS1 = set(s1)
    setS2 = set(s2)
    intersection = setS1.intersection(setS2)
    union = setS1.union(setS2)
    return len(intersection)/len(union)



def findsim(paragraphs,threshold = 0.9):
    tmp = []
    for i in range(1,len(paragraphs)):
        for j in range(i+1,len(paragraphs)):
            s1 = shingles(paragraphs[i])
            s2 = shingles(paragraphs[j])
            a = Jiccard(s1,s2)
            if a > threshold:
                tmp.append((i,j,a))

    return tmp
print(findsim(d))




