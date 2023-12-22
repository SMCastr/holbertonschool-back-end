#!/usr/bin/python3
"""
Python script that, using a REST API, exports data in JSON format
for tasks owned by a given employee.

Requirements: Records all tasks that are owned by this employee
and exports to JSON.

Format must be: { "USER_ID": [ {"task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME},
                {"task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME}, ... ]}
"""

import json
import requests
from sys import argv
from collections import OrderedDict
from typing import List, Dict


def export_to_json(employee_id: str) -> None:
    """
    Exports tasks owned by a given employee to JSON format.
    Args: employee_id (str): The ID of the employee.
    Returns:None
    """
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()
        username = todos[0]["username"]

        json_filename = "{}.json".format(employee_id)

        tasks_list = []
        for todo in todos:
            task_dict = {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": username
            }
            tasks_list.append(task_dict)

        data_dict = {employee_id: tasks_list}

        with open(json_filename, "w") as jsonfile:
            json.dump(data_dict, jsonfile)

        print("JSON file '{}' created successfully.".format(json_filename))
    else:
        print("Error: Unable to fetch data from API")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit()

    employee_id = argv[1]
    export_to_json(employee_id)
