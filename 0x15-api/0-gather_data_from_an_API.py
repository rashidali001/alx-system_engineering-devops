"""0-gather_data_form_an_API

using request/urllib to gather employee data
"""


if __name__ == "__main__":
    from sys import argv
    from requests import get

    user = argv[1]
    data = get("https://jsonplaceholder.typicode.com/users"+"/"+user)
    data = data.json()
    name = data["name"]
    todo_data = get("https://jsonplaceholder.typicode.com/todos").json()
    completed = 0
    incompleted = 0
    total= 0
    completed_task_title_list = list()
    
    users_todos = list()
    for user_todo in todo_data:
        if user_todo["userId"] == int(user):
            users_todos.append(user_todo)
    
    for task in users_todos:
        if task["completed"] == True:
            completed += 1
            completed_task_title_list.append(task["title"])
        else:
            incompleted += 1
    total = completed + incompleted

    print(f"Employee {name} is done with tasks({completed}/{total}):")
    for title in completed_task_title_list:
        print(f"\t {title}")
        










    

