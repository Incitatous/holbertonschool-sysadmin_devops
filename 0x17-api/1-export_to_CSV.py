#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys
    import csv
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
    with open(givenId + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for key in todos:
            writer.writerow([givenId, username,
                            key.get("completed"), key.get("title")])
