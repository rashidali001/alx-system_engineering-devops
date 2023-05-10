#!/usr/bin/python3
""" 2-export_to_JSON
Exports data from an API to a JSON file
"""


if __name__ == "__main__":
    from urllib import request
    from sys import argv
    import json

    Id = int(argv[1])

    req = request.urlopen(f"https://jsonplaceholder.typicode.com/users/{Id}")
    user_name =  json.loads(req.read().decode("utf-8")).get("name")

    req = request.urlopen("https://jsonplaceholder.typicode.com/todos")
    list_of_users_todo = json.loads(req.read().decode("utf-8"))

    filename = f'{Id}.json'
    user_obj_list = []
    user_obj = {}
    obj_list = {}

    for user in list_of_users_todo:
        if user.get("userId") == Id:
            user_obj["task"] = user.get("title")
            user_obj["completed"] = user.get("completed")
            user_obj["username"] = user_name
            user_obj_list.append(user_obj)

    obj_list[f"{Id}"] = user_obj_list

    with open(filename, "w") as file:
        json.dump(obj_list, file)

