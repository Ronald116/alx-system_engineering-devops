#!/usr/bin/python3
"""Python script to export data in the JSON format
"""

import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'

    response = requests.get(url)
    empUsers = response.json()

    d = {}
    for user in empUsers:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos'
        response = requests.get(url)
        tasks = response.json()
        d[user_id] = []
        for task in tasks:
            d[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })

    with open('todo_all_employees.json', 'w') as file:
        json.dump(d, file)

