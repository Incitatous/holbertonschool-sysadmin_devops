#!/usr/bin/python3
if __name__ == "__main__":
    import json
    import requests
    import sys
    givenId = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users?id=" +
                            str(givenId))
    employee = employee.json()
    username = ""
    for x in employee:
        username = x.get("username")

    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId=" +
                         str(givenId))
    todos = todos.json()
    with open(givenId + '.json', 'w') as jsonfile:
        for key in todos:
            json.dump([givenId, username, key.get("completed"), key.get("title")], jsonfile)
