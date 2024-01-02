#!/usr/bin/python3
""" returns information about employee TODO list progress """
from requests import get
from sys import argv

if __name__ == "__main__":
    response = get("https://jsonplaceholder.typicode.com/todos/")
    data = response.json()
    tasks_completed = 0
    total_tasks = 0
    tasks = []
    respon2 = get("https://jsonplaceholder.typicode.com/users")
    user_data = respon2.json()

    for i in user_data:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    for i in data:
        if i.get('userId') == int(argv[1]):
            total_tasks += 1
            if i.get('completed') is True:
                tasks_completed += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee,
                                                          tasks_completed,
                                                          total_tasks))
    for i in tasks:
        print("\t {}".format(i))
