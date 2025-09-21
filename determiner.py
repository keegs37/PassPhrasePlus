import csv
import random
from object import Object

class Determiner():
    def __init__(self, determiner, compatibility
):
        self.determiner = determiner
        self.compatibility = compatibility

    def __str__(self):
        return f"Determiner({self.determiner}, {self.compatibility})"
def create_determiner(object):
    with open("data/Determiners.csv") as determiners_csv:
        rows = list(csv.DictReader(determiners_csv))
        row = random.choice(rows)
        while row["Compatibility"] == "plural_or_uncount" and object.countability == "countable":
            row = random.choice(rows)
        return Determiner(row["Determiner"], row["Compatibility"])
    