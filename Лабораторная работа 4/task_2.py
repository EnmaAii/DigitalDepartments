# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]

    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=True)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
