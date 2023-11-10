#!/usr/bin/env python3
""" This is the console module
It contains the class:
    -HBNBCommand: the entry point of the command interpreter.
"""


import cmd
import models


class HBNBCommand(cmd.Cmd):
    """ This is the HBNBCommand class """

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Place", "Amenity",
               "Review"]

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

    def do_create(self, class_name):
        """ Execute create command """
        from importlib import import_module
        if not class_name:
            print("** class name missing **")
        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            if class_name != 'BaseModel':
                mod_name = import_module("models." + class_name.lower(), ".")
                class_n = getattr(mod_name, class_name)
                inst = class_n()
                inst.save()
            else:
                inst = models.base_model.BaseModel()
                inst.save()
            print(inst.id)

    def do_show(self, line):
        """ Printing instances based on id """
        if not line:
            print("** class name missing **")
            return
        list_args = line.split()
        if list_args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(list_args) < 2:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        inst_id = list_args[1]
        for obj in objs.keys():
            cls_name, id = obj.split(".")
            if id == inst_id and cls_name == list_args[0]:
                print(objs[obj])
                return
        print("** no instance found **")

    def do_destroy(self, line):
        """ Destroy an instance based on id """
        if not line:
            print("** class name missing **")
            return
        list_args = line.split()
        if list_args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(list_args) < 2:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        inst_id = list_args[1]
        for obj in objs.keys():
            cls_name, id = obj.split(".")
            if id == inst_id and cls_name == list_args[0]:
                del objs[obj]
                models.storage.save()
                return
        print("** no instance found **")

    def do_all(self, class_name):
        """ Print all string representations of instances """
        objs = models.storage.all()
        all_list = []
        if not class_name:
            for obj in objs.keys():
                all_list.append(str(objs[obj]))
            print(all_list)
            return
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        for obj in objs.keys():
            cls_name, id = obj.split(".")
            if cls_name == class_name:
                all_list.append(str(objs[obj]))
        print(all_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
