from urllib import request
import json
import sys

argument = int(sys.argv[1])

resp = request.urlopen('https://jsonplaceholder.typicode.com/users')
resp2 = request.urlopen('https://jsonplaceholder.typicode.com/todos')

html = resp.read().decode("UTF-8")
html2 = resp2.read().decode("UTF-8")

# converts the JSON file to an object literal
data = json.loads(html)
userData = json.loads(html2)

user = ''
totalTasks = 0
finishedTasks = 0

for obj in data:
    if obj['id'] == argument:
        user = obj

for obj in userData:
    if obj['userId'] == argument:
        if obj['completed'] == True:
            finishedTasks += 1
        totalTasks += 1

userName = user['name']

print(f"Employee {userName} "
      f"is done with tasks ({finishedTasks}/{totalTasks}):")

for obj in userData:
    if obj['userId'] == argument:
        if obj['completed'] == True:
            print("\t ", end="")
            print(obj['title'])


