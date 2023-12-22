#!/usr/bin/python3
"""
Python script that, using a REST API, exports data in CSV format
for tasks owned by a given employee.
Requirements:
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
    You must use the REST API:
        https://jsonplaceholder.typicode.com/todos
        https://jsonplaceholder.typicode.com/users
    You must use the module requests and sys
    You must export all data in the CSV file
    You must NOT use the module pandas
    The script must be executable by using the following command:
        ./1-export_to_CSV.py <employee_id>
"""


import csv
from collections import OrderedDict
import json
from sys import argv
import requests



if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit()

    employee_id = argv[1]

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()

        if len(todos) == 0:
            print("No tasks found for employee with ID {}".format(employee_id))
            exit()

        username = todos[0]["username"]

        csv_filename = "{}.csv".format(employee_id)

        with open(csv_filename, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for todo in todos:
                task_completed = str(todo["completed"])
                task_title = todo["title"]

                csv_writer.writerow([employee_id, username, task_completed, task_title])

        print("CSV file '{}' created successfully.".format(csv_filename))
        print("Number of tasks: {}".format(len(todos)))  # Add number of tasks in CSV
        print("User ID: {}".format(employee_id))  # Retrieve user ID
        print("Username: {}".format(username))  # Retrieve username
    else:
        print("Error: Unable to fetch data from API")
