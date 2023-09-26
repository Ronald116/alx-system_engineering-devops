#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    baseUrl = 'https://jsonplaceholder.typicode.com/users'
    empID = sys.argv[1]
    url = baseUrl + "/" + empID

    response = requests.get(url)
    empName = response.json().get('name')

    todoURL = url + "/" + "todos"
    response = requests.get(todoURL)
    tasks = response.json()
    done = 0
    total = 0
    completed = []

    for task in tasks:
        total += 1
        if task.get('completed') is True:
            completed.append(task.get('title'))
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(empName, done, total))

    for task in completed:
        print("\t {}".format(task))

