#!/usr/bin/python3
if __name__ == "__main__":
    import json
    import requests
    import sys
    employee = requests.get("https://jsonplaceholder.typicode.com/users")
    employee = employee.json()
    username = ""
    for x in employee:
        username = x.get("username")
        userid = x.get("id")

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()
    gTasks = []
    metaDict = {}
    for key in todos:
        myDict = {}
        myDict["completed"] = key.get("completed")
        myDict["task"] = key.get("title")
        myDict["username"] = username
        gTasks.append(myDict)
    metaDict[userid] = gTasks

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(metaDict, jsonfile)
