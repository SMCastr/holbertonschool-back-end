#!/usr/bin/python3
"""
Python script that, using a REST API, exports data in CSV format
for tasks owned by a given employee.
"""

import csv
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


        csv_filename = "{}.csv".format(employee_id)


        with open(csv_filename, "w", newline="") as csvfile:

            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)


            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for todo in todos:
                task_completed = str(todo["completed"])
                task_title = todo["title"]

                csv_writer.writerow([employee_id, username, task_completed, task_title])

        print("CSV file '{}' created successfully.".format(csv_filename))
    else:
        print("Error: Unable to fetch data from API")