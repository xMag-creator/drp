"""
connect to device via profinet / txt file ( when changed ).
Read data from it.
Save it to txt / csv / json file.
"""
import os
import time

watched_file = 'test.txt'
name_new_file = 'new_file'
last_modified = os.path.getmtime(watched_file)


def over_write(new_name):
    with open("test.txt", "r") as file:
        dane = file.read()
        print(dane)

    with open(f"{new_name}.txt", 'w') as new_file:
        new_file.write(dane)


if __name__ == '__main__':
    while True:
        if os.path.getmtime(watched_file) > last_modified:
            last_modified = os.path.getmtime(watched_file)
            over_write(name_new_file)
        time.sleep(1)
