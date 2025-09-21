import csv
import random

class Verb(): 

    def __init__(self, verb_base, past, past_participle, gerund, regularity):
        self.verb_base = verb_base
        self.past = past
        self.past_participle = past_participle
        self.gerund = gerund
        self.regularity = regularity

    def __str__(self):
        return f"Verb({self.verb_base}, {self.past}, {self.past_participle}, {self.gerund}, {self.regularity})"

def create_verb():
    with open("data/Verbs.csv") as verbs_csv:
        rows = list(csv.DictReader(verbs_csv))
        row = random.choice(rows)
        return Verb(row["Verb_Base"], row["Past"], row["PastParticiple"], row["Gerund"], row["Regularity"])
    

print(create_verb())