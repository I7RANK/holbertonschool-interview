#!/usr/bin/python3
""" """

# Funciona peroo no bloquea el Ctrl + C para ambos programas
# por lo que se detiene el que envia las señales
# y ese detiene el otro por el EOF
import signal
import sys
from time import sleep

read = True
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

'''
# get the original handler of SIGINT signal
original_sigint_handler = signal.getsignal(signal.SIGINT)

def signal_handler(sig, frame):
    print("File size:", sizes)
    print_dict(status_code_counter)

    # Then set the handler to default
    signal.signal(signal.SIGINT, original_sigint_handler)

    # Then raise the signal again
    signal.raise_signal(signal.SIGINT)


signal.signal(signal.SIGINT, signal_handler)
'''


def print_dict(dicti):
    for k, v in dicti.items():
        if v > 0:
            print(k, v)

try:
    for input_format in sys.stdin:
        counter += 1

        input_format_list = input_format.split(" ")

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
