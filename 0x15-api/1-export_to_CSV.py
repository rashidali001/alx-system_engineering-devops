#!/usr/bin/python3
'''
 Using the request module to get data from an API 
'''


if __name__ == "__main__": # Prevents our code from being imported
    from urllib import request
    import csv
    import sys
    import json

    
    id = int(sys.argv[1])

    req = request.urlopen("https://jsonplaceholder.typicode.com/users")
    req_json = req.read().decode('utf=8')
    users_list = json.loads(req_json)

    completed_tasks = 0
    total_tasks = 0

    for user in users_list:
        if user.get("id") == id:
            name = user.get("name")

    req = request.urlopen("https://jsonplaceholder.typicode.com/todos")
    req_json = req.read().decode("utf-8")
    users_tasks = json.loads(req_json)
    
    user_task_in_list = []
    for user_task in users_tasks:
        if user_task.get("userId") == id:
            new_dict = {}
            new_dict['USER_ID'] = user_task.get("userId")
            new_dict['USERNAME'] = name
            new_dict['TASK_COMPLETED_STATUS'] = user_task.get("completed")
            new_dict['TASK_TITLE'] = user_task.get("title")
            user_task_in_list.append(new_dict)
    
    filename = f"{id}.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=user_task_in_list[0].keys())

        for row in user_task_in_list:
            writer.writerow(row)
