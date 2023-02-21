#!/usr/bin/python3
''' Using the request module to get data from an API '''


if __name__ == "__main__": # Prevents our code from being imported
    from urllib import request
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
    
    for user_task in users_tasks:
        if user_task.get("userId") == id:
            total_tasks += 1
            if user_task.get("completed") == True:
                completed_tasks += 1

    print(f"Employee {name} is done with tasks({completed_tasks}/{total_tasks}):")

    for user_task in users_tasks:
        if user_task.get("userId") == id:
            if user_task.get("completed") == True:
                
                print("\t" , user_task.get("title"))           
            
