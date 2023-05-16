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
    
    users_todos = list()
    for user_todo in todo_data:
        if user_todo["userId"] == int(user):
            users_todos.append(user_todo)
    
    print(name)
    for task in users_todos:
        if task["completed"] == True:
            completed += 1
        else:
            incompleted += 1
    
    print(f"completed taks: {completed}")
    print(f"Incompleted taks: {incompleted}")


        
        











    

