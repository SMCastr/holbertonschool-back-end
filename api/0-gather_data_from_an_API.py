import requests
from sys import argv


def gather_data_from_api(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    if user_response.status_code == 200:
        employee_name = user_data.get("username", "")
        if not employee_name:
            print("Error: Unable to fetch employee name.")
            return

        todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        todo_response = requests.get(todo_url)

        if todo_response.status_code == 200:
            todos = todo_response.json()

            if todos:
                total_tasks = len(todos)
                completed_tasks = sum(1 for todo in todos if todo["completed"])

                print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

                for todo in todos:
                    if todo["completed"]:
                        print(f"\t{todo['title']}")
            else:
                print(f"Employee {employee_name} has no tasks.")
        else:
            print("Error: Unable to fetch TODO list data from API")
    else:
        print("Error: Unable to fetch user data from API")


if __name__ == "__main__":
    if len(argv) != 2:
        print(f"Usage: {argv[0]} employee_id")
    else:
        employee_id = argv[1]
        gather_data_from_api(employee_id)
