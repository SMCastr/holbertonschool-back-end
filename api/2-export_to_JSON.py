#!/usr/bin/python3
"""
Python script that, using a REST API, exports data in JSON format
for tasks owned by a given employee.

Requirements: Records all tasks that are owned by this employee
and exports to JSON.

Format must be: { "USER_ID": [{"task": "TASK_TITLE",
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


def export_to_json(employee_id: List[Dict[str, str]]) -> None:
    """
    Exports tasks owned by a given employee to JSON format.
    Args:
        employee_id (List[Dict[str, str]]): The list of employee IDs and names.
    Returns:
        None
    """
    for employee in employee_id:
        employee_id = employee["id"]
        employee_name = employee["name"]

        url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

        response = requests.get(url)

        if response.status_code == 200:
            todos = response.json()

            json_filename = "{}.json".format(employee_id)

            tasks_list = []
            for todo in todos:
                task_dict = {
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": employee_name
                }
                tasks_list.append(task_dict)

            data_dict = {str(employee_id): tasks_list}

            with open(json_filename, "w") as jsonfile:
                json.dump(data_dict, jsonfile)

            print("JSON file '{}' created successfully.".format(json_filename))
        else:
            print("Error: Unable to fetch data from API")

# User ID's value is a list of dicts
employee_id: List[Dict[str, str]] = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]

# All tasks found in list of dicts
tasks = [{"task": "Task 1", "completed": True}, {"task": "Task 2", "completed": False}]

# Ensure employee_id is a list of dicts
if isinstance(employee_id, dict):
    employee_id = [employee_id]

export_to_json(employee_id)
