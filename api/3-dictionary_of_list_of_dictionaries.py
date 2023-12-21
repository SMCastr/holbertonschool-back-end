#!/usr/bin/python3
"""
Export data in the JSON format

Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [ {"task": "TASK_TITLE", "completed":
    TASK_COMPLETED_STATUS, "username": "USERNAME"}}, {"task":
    "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}
    File name must be: USER_ID.json
You must use the REST API:
    https://jsonplaceholder.typicode.com/todos
    https://jsonplaceholder.typicode.com/users
    You must use the module requests and sys
    You must export all data in the JSON format
    You must NOT use the module pandas
The script must be executable by using the following command:
./2-export_to_JSON.py <employee_id>

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
