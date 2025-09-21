import csv
import random

class Determiner():
    def __init__(self, determiner, compatibility
):
        self.determiner = determiner
        self.compatibility = compatibility

    def __str__(self):
        return f"Determiner({self.determiner}, {self.compatibility})"
def create_determiner():
    with open("data/Determiners.csv") as determiners_csv:
        rows = list(csv.DictReader(determiners_csv))
        row = random.choice(rows)
        return Determiner(row["Determiner"], row["Compatibility"])
    

print(create_determiner())