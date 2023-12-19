#!/usr/bin/python3
"""
Export data in the JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users").json()

    all_data = {}
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        tasks = requests.get(base_url + "todos", params={"userId": user_id}).json()

        task_list = []
        for task in tasks:
            task_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            })

        all_data[user_id] = task_list

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file)