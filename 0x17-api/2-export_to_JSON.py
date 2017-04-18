#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""
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
    gTasks = []
    for key in todos:
        myDict = {}
        myDict["completed"] = key.get("completed")
        myDict["task"] = key.get("title")
        myDict["username"] = username
        gTasks.append(myDict)

    with open(givenId + '.json', 'w') as jsonfile:
        json.dump({givenId: gTasks}, jsonfile)
