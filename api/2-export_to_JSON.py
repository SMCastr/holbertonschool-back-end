#!/usr/bin/python3
"""
Python script that, using a REST API, exports data in JSON format
for tasks owned by a given employee.

Requirements: Records all tasks that are owned by this employee
and exports to JSON.

Format must be: { "USER_ID": [{"task": "TASK_TITLE",
            "completed": TASK_COMPLETED_STATUS,
            "username": USERNAME},
]}
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

        api_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
        api_url2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

        response = requests.get(api_url).json()
        EMPLOYEE_NAME = response.get('username')

        response = requests.get(api_url2).json()

        json_filename = "{}.json".format(employee_id)

        tasks_list = []
        for info in response:
            task_dict = {
                "task": info.get('title'),
                "completed": info.get('completed'),
                "username": EMPLOYEE_NAME
            }
            tasks_list.append(task_dict)

        data_dict = {str(employee_id): tasks_list}

        with open(json_filename, "w", encoding="utf-8") as jsonfile:
            json.dump(data_dict, jsonfile)

        print("JSON file '{}' created successfully.".format(json_filename))
        print("Number of tasks: {}".format(len(tasks_list)))
        print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                              len(tasks_list),
                                                              len(response)))
        employee_done_tasks = []
        for task in tasks_list:
            if task.get('completed') is True:
                employee_done_tasks.append(task)
                print("\t {}".format(task.get('title')))
        print("\n")
        
if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(api_url).json()

    employee_id = []
    for user in response:
        employee_id.append({"id": user.get('id'), "name": user.get('name')})

    export_to_json(employee_id)

