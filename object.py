import csv
import random

class Object(): 

    def __init__(self, object, countability, default_number):
        self.object = object
        self.countability = countability
        self.default_number = default_number

    def __str__(self):
        return f"Object({self.object}, {self.countability}, {self.default_number})"

def create_object():
    with open("data/Objects.csv") as objects_csv:
        rows = list(csv.DictReader(objects_csv))
        row = random.choice(rows)
        return Object(row["Object"], row["Countability"], row["Default_Number"])
    

print(create_object())