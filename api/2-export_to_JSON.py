#!/usr/bin/python3
"""
Python script that, using a REST API, exports data in JSON format for tasks owned by a given employee.
"""

import json
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

        # Define the JSON file name
        json_filename = "{}.json".format(employee_id)

        # Create a list of tasks in the required format
        tasks_list = [{"task": todo['title'], "completed": todo['completed'], "username": username} for todo in todos]

        # Create a dictionary with the employee ID as the key and the tasks list as the value
        data_dict = {employee_id: tasks_list}

        # Write the data to the JSON file
        with open(json_filename, 'w') as jsonfile:
            json.dump(data_dict, jsonfile)

        print("JSON file '{}' created successfully.".format(json_filename))
    else:
        print("Error: Unable to fetch data from API")
