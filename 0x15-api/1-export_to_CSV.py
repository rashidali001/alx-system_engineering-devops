#!/usr/bin/python3
""" 1-export_to_CSV.py
Export data to CSV
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    Employee_Id = int(argv[1])
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    Employee_todos = list()

    for obj in todos:
        if obj["userId"] == Employee_Id:
            Employee_todos.append(obj)

    name = requests.get(
        "https://jsonplaceholder.typicode.com/users" + f"/{Employee_Id}"
    ).json()["name"]

    filename = f"{Employee_Id}" + ".csv"

    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_ALL)

        for task in Employee_todos:
            writer.writerow(
                [
                    f"{task['userId']}",
                    f"{name}",
                    f"{task['completed']}",
                    f"{task['title']}",
                ]
            )
