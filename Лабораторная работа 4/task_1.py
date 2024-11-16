# TODO решите задачу
import json

IMPORT_FILE = "input.json"

def task() -> float:
    with open(IMPORT_FILE) as f:
        data = json.load(f)
        total_sum = 0.0
        for i in data:
            if "score" in i and "weight" in i:
                total_sum += i["score"] * i["weight"]
    return round(total_sum, 3)


print(task())
