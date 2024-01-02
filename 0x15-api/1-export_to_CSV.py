#!/usr/bin/python3
""" returns information about employee TODO list progress """
from requests import get
from sys import argv
import csv


if __name__ == "__main__":
    response = get("https://jsonplaceholder.typicode.com/todos/")
    data = response.json()
    row = []
    respon2 = get("https://jsonplaceholder.typicode.com/users")
    user_data = respon2.json()

    for i in user_data:
        if i['id'] == int(argv[1]):
            employee = i['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        written = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in data:
            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.append(i['completed'])
                row.append(i['title'])

                written.writerow(row)
