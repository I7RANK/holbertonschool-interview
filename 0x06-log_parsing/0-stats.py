#!/usr/bin/python3
""" This module contains the Log parsing script """


import sys


counter = 0
sizes = 0

status_code_counter = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_dict(dicti):
    for k, v in dicti.items():
        if v > 0:
            print(k, v)


try:
    for input_format in sys.stdin:
        counter += 1

        input_format_list = input_format.split()

        if len(input_format_list) == 9:
            if input_format_list[7] in status_code_counter:
                status_code_counter[input_format_list[7]] += 1
            sizes += int(input_format_list[8])

            if counter == 10:
                print("File size:", sizes)
                print_dict(status_code_counter)
                counter = 0
finally:
    print("File size:", sizes)
    print_dict(status_code_counter)
