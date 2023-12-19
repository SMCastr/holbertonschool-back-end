# holbertonschool-back-end
api

## Description
This project is about building an API using Flask and Python.

## Table of contents
Files | Description
----- | -----------
[models](./models) | Contains the classes used for the API
[views](./views) | Contains the routes for the API
[app.py](./app.py) | Main file for the API
[setup_mysql_dev.sql](./setup_mysql_dev.sql) | SQL script to create the database and tables
[setup_mysql_test.sql](./setup_mysql_test.sql) | SQL script to create the database and tables for testing
[setup_mysql_prod.sql](./setup_mysql_prod.sql) | SQL script to create the database and tables for production

# holbertonschool-back-end
api

## Description
This project is about building an API using Flask and Python.

## Table of contents
Files | Description
----- | -----------
[0-simple_api.py](./0-simple_api.py) | Script that starts a Flask web application
[1-export_to_CSV.py](./1-export_to_CSV.py) | Script that exports data in the CSV format
[2-export_to_JSON.py](./2-export_to_JSON.py) | Script that exports data in the JSON format
[3-dump_to_JSON.py](./3-dump_to_JSON.py) | Script that exports data in the JSON format

## Usage
```
$ ./0-simple_api.py
```
```
$ ./1-export_to_CSV.py <user_id>
```
```
$ ./2-export_to_JSON.py <user_id>
```
```
$ ./3-dump_to_JSON.py
```

## Author
Sweety Castro 

## License
 anonymous
## Acknowledgements
I am grateful, with the opportunity to learn software development.

## Usage
To run the API, execute the following command:
```
python3 -m api.v1.app
```
To run the tests, execute the following command:
```
python3 -m unittest discover tests
```
To run the tests with coverage, execute the following command:
```
python3 -m unittest discover tests --coverage
```
To run the tests with coverage and generate a report, execute the following commands:
```
python3 -m unittest discover tests --coverage
coverage html
```

### Status
```
GET /api/v1/status
```
Returns the status of the API.

## Author
Sweety Castro 

## License
 anonymous
## Acknowledgements
I am grateful, with the opportunity to learn software development.