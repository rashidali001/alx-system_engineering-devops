#!/usr/bin/python3
""" 2-export_to_JSON.py
Export data to JSON file
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    Employee_Id = int(argv[1])
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    Employee_todos = list()

    for obj in todos:
        if obj["userId"] == Employee_Id:
            Employee_todos.append(obj)

    username = requests.get(
        "https://jsonplaceholder.typicode.com/users" + f"/{Employee_Id}"
    ).json()["username"]

    filename = f"{Employee_Id}" + ".json"

    list_to_json = list()

    for task in Employee_todos:
        object_to_list = dict()
        object_to_list["task"] = task["title"]
        object_to_list["completed"] = task["completed"]
        object_to_list["username"] = username
        list_to_json.append(object_to_list)

    export = {f"{str(Employee_Id)}": list_to_json}

    with open(filename, mode="w") as json_file:
        json.dump(export, json_file)
