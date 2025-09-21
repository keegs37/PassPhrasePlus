import csv
import random

class Subject():
    def __init__(self, subject, person, number):
        self.subject = subject
        self.person = person
        self.number = number

    def __str__(self):
        return f"Subject({self.subject}, {self.person}, {self.number})"
def create_subject():
    with open("data/Subjects.csv") as subjects_csv:
        rows = list(csv.DictReader(subjects_csv))
        row = random.choice(rows)
        return Subject(row["Subject"], row["Person"], row["Number"])
    

print(create_subject())