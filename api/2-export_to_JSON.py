#!/usr/bin/python3
"""
Python script that, using a REST API, exports data in JSON format for tasks owned by a given employee.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit()

    employee_id = argv[1]

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    response = requests.get(url)

    if response.status_code == 200:

        todos = response.json()

        username = todos[0]["username"]

        json_filename = "{}.json".format(employee_id)

        tasks_list = [{"task": todo["title"], "completed": todo["completed"], "username": username} for todo in todos]

        data_dict = {employee_id: tasks_list}

        with open(json_filename, "w") as jsonfile:
            json.dump(data_dict, jsonfile)

        print("JSON file '{}' created successfully.".format(json_filename))
    else:
        print("Error: Unable to fetch data from API")