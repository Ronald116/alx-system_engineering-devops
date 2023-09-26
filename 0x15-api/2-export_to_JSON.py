#!/usr/bin/python3
"""Python script to export data in the JSON format
"""

import json
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
    dictStruct = {empID: []}

    for task in tasks:
        dictStruct[empID].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": empUserName
            })

    with open(("{}.json".format(empID)), 'w') as file:
        json.dump(dictStruct, file)
