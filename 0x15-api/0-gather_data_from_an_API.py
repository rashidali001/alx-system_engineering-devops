#!/usr/bin/python3
"""

0-gather_data_from_an_API - gets data from an API
A python script that takes an argument
from the command line and uses its urllib
package to fetch data from an API

"""


if __name__ == "__main__":
    import json
    from urllib import request
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
        if obj.get('id') == argument:
            user = obj

    for obj in userData:
        if obj.get('userId') == argument:
            if obj.get('completed') == True:
                finishedTasks += 1
            totalTasks += 1

    userName = user.get('name')

    print(f"Employee {userName} "
          f"is done with tasks ({finishedTasks}/{totalTasks}):")

    for obj in userData:
        if obj.get('userId') == argument:
            if obj.get('completed') == True:
                print("\t ", end="")
                print(obj['title'])
