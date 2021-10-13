#!/usr/bin/env python3

import subprocess 
import sys
import os


def clean():
    cwd = os.getcwd()
    dir_list = os.listdir(cwd)

    files_to_remove = []
    for file in dir_list:
        if ".dfa.pdf" in file or ".nfa.pdf" in file:
            files_to_remove.append(file)

    # none to delete
    if len(files_to_remove) == 0:
        print("Nothing to clean")
        return

    # confirm deletion
    response = input("Confirm deleting: " + str(files_to_remove) + "? [y/n]: ")
    if response == "y":
        for file in files_to_remove:
            os.remove(file)
        return
    else:
        print("Clean aborted, not removing files")
    return

# def checkall():
#     # cwd = os.getcwd()
#     # dir_list = os.listdir(cwd)
#     # machines = []
#     # for file in dir_list:
#     #     if file.endswith(".nfa") or file.endswith(".dfa"):
#     #         machines.append(file)

#     # for machine in machines:
#     #     subprocess

def pdfall():
    cwd = os.getcwd()
    dir_list = os.listdir(cwd)
    machines = []
    for file in dir_list:
        if file.endswith(".nfa") or file.endswith(".dfa"):
            machines.append(file)

    for machine in machines:
        subprocess.run(["/cs/student/emre/bin/mentor", machine, "graph", machine +".pdf"])

    return


def main():
    if sys.argv[1] == "clean":
        return clean()

    elif sys.argv[1] == "pdfall":
        return pdfall()
    else:
        print("Invalid argument")
        return


if __name__ == '__main__':
    main()