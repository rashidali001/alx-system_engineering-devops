"""0-gather_data_form_an_API

using request/urllib to gather employee data
"""


if __name__ == "__main__":
    from sys import argv
    from requests import get

    user = argv[1]
    data = get("https://jsonplaceholder.typicode.com/users"+"/"+user)
    data = data.json()
    print(data["username"])











    

