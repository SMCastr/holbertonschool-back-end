#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit()

    # Get the employee ID from the command-line arguments
    employee_id = argv[1]

    # URL for the REST API endpoint with the employee ID
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract JSON data from the response
        todos = response.json()

        # Get the employee's name from the first TODO item (assuming it's the same for all)
        employee_name = todos[0]['username']

        # Get the total number of tasks and the number of completed tasks
        total_tasks = len(todos)
        completed_tasks = sum(1 for todo in todos if todo['completed'])

        # Display the employee's TODO list progress
        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, completed_tasks, total_tasks))

        # Display the titles of completed tasks with proper indentation
        for todo in todos:
            if todo['completed']:
                print("\t {}".format(todo['title']))
    else:
        print("Error: Unable to fetch data from API")
