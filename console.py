#!/usr/bin/env python3
""" This is the console module
It contains the class:
    -HBNBCommand: the entry point of the command interpreter.
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """ This is the HBNBCommand class """

    prompt = "(hbnb)"

    def do_EOF(self, line):
        """ Execute EOF command """
        return True

    def do_quit(self, line):
        """ Execute quit command """
        return True

    def do_help(self, command):
        """ Execute help command with different options """
        if command == 'quit':
            print('quit command to exit the program\n')
        if command == 'EOF':
            print('EOF (Ctrl +D) command to exit the program\n')
        if not command:
            print("\nDocumented commands (type help <topic>):\n\
========================================\n\
EOF  help  quit\n")

    def emptyline(self):
        """ Overridding the Cmd.emptyline() method """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
