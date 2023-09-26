#!/usr/bin/python3
"""
Python script to export data in the CSV format
"""

import requests
import sys


if __name__ == "__main__":
    baseUrl = 'https://jsonplaceholder.typicode.com/users'
    empID = sys.argv[1]
    url = baseUrl + "/" + empID

    response = requests.get(url)
    empUserName = response.json().get('username')

    todoURL = url + "/" + "todos"
    response = requests.get(todoURL)
    tasks = response.json()

    with open(("{}.csv".format(empID)), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"'.format(
                empID, empUserName, task.get('completed'), task.get('title')))
