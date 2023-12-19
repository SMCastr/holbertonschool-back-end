#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

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

        employee_name = todos[0]["username"]

        total_tasks = len(todos)
        completed_tasks = sum(1 for todo in todos if todo["completed"])


        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, completed_tasks, total_tasks))


        for todo in todos:
            if todo["completed"]:
                print("\t {}".format(todo["title"]))
    else:
        print("Error: Unable to fetch data from API")