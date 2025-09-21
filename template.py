import csv
import random

class Template():
    def __init__(self, tense, aspect, pattern):
        self.tense = tense
        self.aspect = aspect
        self.pattern = pattern

    def __str__(self):
        return f"Template({self.tense}, {self.aspect}, {self.pattern})"
def create_template():
    with open("data/Templates.csv") as templates_csv:
        rows = list(csv.DictReader(templates_csv))
        row = random.choice(rows)
        return Template(row["Tense"], row["Aspect"], row["Pattern"])
    
