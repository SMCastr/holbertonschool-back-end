#!/usr/bin/python3
"""
Python script that, using a REST API, exports data in CSV format for tasks owned by a given employee.
"""

import csv
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

        # Get the employee's username from the first TODO item (assuming it's the same for all)
        username = todos[0]['username']

        # Define the CSV file name
        csv_filename = "{}.csv".format(employee_id)

        # Open the CSV file in write mode
        with open(csv_filename, 'w', newline='') as csvfile:
            # Create a CSV writer object
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

            # Write the header row to the CSV file
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write each task as a row in the CSV file
            for todo in todos:
                # Extract relevant information from the TODO item
                task_completed = str(todo['completed'])
                task_title = todo['title']

                # Write the row to the CSV file
                csv_writer.writerow([employee_id, username, task_completed, task_title])

        print("CSV file '{}' created successfully.".format(csv_filename))
    else:
        print("Error: Unable to fetch data from API")
