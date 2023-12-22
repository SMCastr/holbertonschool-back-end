#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about "his/her" (Todo) list progress.
Requirements:
The script must display on the standard output the employee (Todo)
list progress in this exact format:
First line:
Employee EMPLOYEE_NAME is done with tasks (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    EMPLOYEE_NAME: name of the employee
    NUMBER_OF_DONE_TASKS: number of completed tasks
    TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the
    sum of completed and non-completed tasks
Second and N next lines display the title of completed tasks:
    TASK_TITLE: title of the task
Tasks must be sorted by completed status (completed last) and then
by the task id (ascending)
You must use the REST API:
    https://jsonplaceholder.typicode.com/todos
    https://jsonplaceholder.typicode.com/users
You must NOT use the module pandas
To format records displayed in the terminal, please use this
format:
    <USER_NAME> [<TASK_COMPLETED_STATUS>] <TASK_TITLE>
The script must be executable by using the following command:
    ./0-gather_data_from_an_API.py <employee_id>
"""


import requests
from sys import argv
from typing import List, Dict
from collections import OrderedDict


def gather_data_from_api(employee_id: str) -> None:
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    if user_response.status_code == 200:
        employee_name = user_data.get("name", "")
        if not employee_name:
            print("Error: Unable to fetch employee name.")
            return

        todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        todo_response = requests.get(todo_url)

        if todo_response.status_code == 200:
            todos = sorted(todo_response.json(), key=lambda x: (x["completed"], x["id"]))

            if todos:
                total_tasks = len(todos)
                completed_tasks = sum(1 for todo in todos if todo["completed"])

                print("Employee {} is done with tasks ({}/{}):".format(
                    employee_name, completed_tasks, total_tasks))

                for idx, todo in enumerate(todos, start=1):
                    print("\t {}. [{}] {}".format(idx, "OK" if todo["completed"] else "Not OK", todo["title"]))
            else:
                print("Employee {} has no tasks.".format(employee_name))
        else:
            print("Error: Unable to fetch TODO list data from API")
    else:
        print("Error: Unable to fetch user data from API")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit()

    employee_id = argv[1]
    gather_data_from_api(employee_id)
