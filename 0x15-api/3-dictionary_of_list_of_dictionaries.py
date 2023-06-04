#!/usr/bin/python3
""" 2-export_to_JSON.py
Export data to JSON file
"""
import json
import requests


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    all_Employess = dict()
    all_Employess_dict = dict()

    for user in users:
        todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
        user_task = list()
        for task in todos:
            if task["userId"] == user["id"]:
                user_task.append(task)

        user_list = list()
        for task in user_task:
            user_dict = dict()
            user_dict["username"] = user["username"]
            user_dict["task"] = task["title"]
            user_dict["completed"] = task["completed"]
            user_list.append(user_dict)

        all_Employess_dict[f"{user['id']}"] = user_list

    with open("todo_all_employees.json", mode="w") as employees:
        json.dump(all_Employess_dict, employees)
