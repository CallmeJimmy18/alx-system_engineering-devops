#!/usr/bin/python3
""" returns information about employee TODO list progress """
from requests import get
from sys import argv
import csv
import json


if __name__ == "__main__":
    response = get("https://jsonplaceholder.typicode.com/todos/")
    data = response.json()
    row = []
    respon2 = get("https://jsonplaceholder.typicode.com/users")
    user_data = respon2.json()
    all_employees = {}

    for i in user_data:
        employee = i['username']
        id_no = i['id']

        usrtasks = []
        for i in data:
            if i['userId'] == id_no:
                task_data = {"username": employee,
                             "task": i['title'],
                             "completed": i['completed']
                             }
                usrtasks.append(task_data)

        all_employees[id_no] = usrtasks

    with open("todo_all_employees.json", 'w') as fle:
        json.dump(all_employees, fle)
