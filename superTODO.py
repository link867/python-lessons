#!/usr/bin/python3

import signal

def parse_input(data):
    data = data.rstrip()

    if not data:
        show_help()

    #if data is not str:
    #    print(type(data))
    #    print("Invalid Input [" + data + "]")
    #    show_help()

    #    return

    split_data = data.split( )

    if split_data[0] not in valid_commands:
        print("Invalid input [%s]\n" % (data))
        show_help()

        return

    arg = ''
    arg2 = ''

    if len(split_data) > 1:
        arg = split_data[1]

        if len(split_data) > 2:
            arg2 = split_data[2]

    run_command(split_data[0], arg, arg2)


def run_command(cmd, arg, arg2):
    if cmd == 'help':
        show_help()

    elif cmd == 'show':
        if not arg:
            print("\'show\' requires an arg: to-do item")

            return

        show_todo(arg)

    elif cmd == 'list':
        list_todo()

    elif cmd == 'new':
        if not arg:
            print("\'new\' requires and argument: to-do item")

            return


        new_todo(arg, '')

    elif cmd == 'save':
        if not arg:
            print("\'save\' requires and argument: file name")

            return

        save_todo(arg)

    elif cmd == 'load':
        if not arg:
            print("\'load\' requires and argument: file name")

            return

        load_todo(arg)


    return


def show_todo(arg):
    #print("This is your todo")

    if arg not in todos:
        print(arg + " not found in list of to-dos")

        return

    print("%s: %s" % (arg, todos[arg]))

    return


def list_todo():
    if not todos:
        print("You have no to-dos!")

        return

    print("These are your todos:")

    i = 1
    for key, value in todos.items():
        print("%s. %s" % (i, key))
        i += 1

    return


def new_todo(arg, v):
    global todos, change_flag

    while True:
        desc = input("Enter a description for %s: " % arg)

        if not desc:
            print("Please enter a description!\n")
            continue

        break

    print("Creating new todo named " + arg)

    todos[arg] = desc

    change_flag = 1

    return

def save_todo(arg):
    global todos, change_flag

    print("Saving to a file will overwrite the contents.")
    yor = input("Are you sure you want to continue?[y/n]: ")
    while True:
        if not (yor == 'y' or yor == 'n'):
            yor = input("Please enter 'y' or 'n': ")
            continue

        if yor == 'n':
            return

        break

    f = open(arg, 'w')

    for key, value in todos.items():
        f.write("%s:%s\n" % (key, value))

    f.close()

    change_flag = 0

    print("To-do list saved in %s successfully" % arg)

    return

def load_todo(arg):
    global todos

    f = open(arg, 'r')

    for line in f:
        line = line.rstrip()

        if not line:
            continue

        sline = line.split(':')
        todos[sline[0]] = sline[1]

    print("To-do list loaded successfully")

    return


def show_help():
    ##print("Valid commands: " + '%s\n' % ', '.join(map(str, valid_commands)))
    print("Valid commands: ")

    for key, value in valid_commands.items():
        print("%s: %s" % (key, value))

    return

def exit_app(s, f):
    if s or f:
        print("\nCTRL-C detected, exiting application")

    if change_flag == 1:
        print("Changes have been made and not saved to a file.")
        syor = input("Would you like to save to a file?[y/n]: ")

        while True:
            syor = syor.rstrip()
            if not (syor == 'y' or syor == 'n'):
                syor = input("Please enter 'y' or 'n': ")
                syor = syor.rstrip()
                continue

            if syor == 'n':
                break

            while True:
                file = input("Please enter the file name you wish to save to: ")
                file = file.rstrip()

                if not file:
                    print("Please enter a file name")
                    continue

                save_todo(file)
                break

            break

    exit(0)



# Main #
signal.signal(signal.SIGINT, exit_app)

change_flag = 0
todos = {}

valid_commands = {
    'help' : "'help' Display help page",
    'show' : "'show <to-do item>' Show description for a to-do item",
    'list' : "'list' List to-do items",
    'new'  : "'new <to-do item>' Create a new to-do item",
    'save' : "'save <file name>' Save current to-do list to file",
    'load' : "'new <to-do item>' Load a to-do list from a file. Format: 'item:description'"
}


while True:
    user_input = input("SuperTODO> ")

    if user_input == "quit" or user_input == "exit":
        exit_app('', '')

    parse_input(user_input)


