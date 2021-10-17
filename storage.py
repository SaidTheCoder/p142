import csv
from pprint import pprint
article=[]
with open("articles.csv", newline ="",encoding="utf8") as f:
    reader=csv.reader(f)
    data = list(reader)
    articles=data[1:]

