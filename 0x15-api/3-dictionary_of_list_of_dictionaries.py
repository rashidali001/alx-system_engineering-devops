#!/usr/bin/python3
""" 3-dictionary_of_list_of_dictionaries
Stores all task users with respective Id's in a dictionary
"""


if __name__ == "__main__":
    from urllib import request
    import json

    req = request.urlopen("https://jsonplaceholder.typicode.com/users")
    Id_s = []
    names = []
    user_list = json.loads(req.read().decode("utf-8"))

    for user in user_list:
        Id_s.append(user.get("id"))
        names.append(user.get("name"))
    
    req = request.urlopen("https://jsonplaceholder.typicode.com/todos")
    user_todos = json.loads(req.read().decode("utf-8"))
    all_users_tasks = {}
    arr_of_user = []
    user_obj = {}
    
    count = 0
    index = 1

    for user in user_todos:
        if user.get("userId") == Id_s[count]:
            user_obj["username"] = names[count]
            user_obj["task"] = user.get("title")
            user_obj["completed"] = user.get("completed")

        arr_of_user.append(user_obj)    
    
    print(arr_of_user)