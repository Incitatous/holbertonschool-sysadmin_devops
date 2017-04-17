#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys
    givenId = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users?id=" +
                            str(givenId))
    employee = employee.json()
    name = ""
    for x in employee:
        name = x['name']

    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId=" +
                         str(givenId))
    todos = todos.json()
    done = 0
    total = 0
    doneTasks = ""
    for key in todos:
        total += 1
        if(key['completed'] is True):
            doneTasks = doneTasks+key['title'] + "\n\t"
            done += 1

    print("Employee {:s} is done with tasks({:d}/{:d}):"
          .format(name, done, total))
    print("\t{:s}".format(doneTasks.rstrip()))
