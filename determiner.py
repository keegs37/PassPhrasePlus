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
        def is_compatible(row):
            comp = row["Compatibility"]
            if object.countability == "uncountable":
                return comp in {"any", "uncount", "plural_or_uncount"}
            if object.default_number == "plural":
                return comp in {"any", "plural_any", "plural_count", "plural_or_uncount"}
            return comp in {"any", "singular_any", "singular_count"}
        filtered = [row for row in rows if is_compatible(row)]
        if not filtered:
            filtered = [row for row in rows if row["Compatibility"] == "any"]
        chosen = random.choice(filtered)
        return Determiner(chosen["Determiner"], chosen["Compatibility"])
    