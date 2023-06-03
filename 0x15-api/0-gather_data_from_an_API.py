#!/usr/bin/python3
''' 0-gather_data_from_an_API 
Gather data from an API
'''
import requests
from sys import argv


if __name__ == "__main__":
    Employee_Id = int(argv[1])
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    Employee_todos = list()

    for obj in todos:
        if obj["userId"] == Employee_Id:
            Employee_todos.append(obj)

    completed = 0
    incomplete = 0
    completed_task = list()

    for task in Employee_todos:
        if task["completed"] == False:
            incomplete += 1
        if task["completed"] == True:
            completed += 1
            completed_task.append(task["title"])

    name = requests.get(
        "https://jsonplaceholder.typicode.com/users" + f"/{Employee_Id}"
    ).json()["name"]
    total = completed + incomplete

    print(f"Employee {name} is done with tasks({completed}/{total}):")
    for task in completed_task:
        print(f"\t{task}")
