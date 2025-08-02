import json
import os

FILE = "records.json"

def read_records():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return {}
def save_records(records):
    with open(FILE, "w") as file:
        json.dump(records, file, indent=4)

def calc_average_and_grade(subject_scores):
    if not subject_scores:
        return 0.0, ""
    
    total = sum(subject_scores.values())
    average = round(total / len(subject_scores), 2)
    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    
    return average, grade