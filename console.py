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
    objs = models.storage.all()

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
        inst_id = list_args[1]
        for obj in HBNBCommand.objs.keys():
            cls_name, id = obj.split(".")
            if id == inst_id and cls_name == list_args[0]:
                print(HBNBCommand.objs[obj])
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
        inst_id = list_args[1]
        for obj in HBNBCommand.objs.keys():
            cls_name, id = obj.split(".")
            if id == inst_id and cls_name == list_args[0]:
                del HBNBCommand.objs[obj]
                models.storage.save()
                return
        print("** no instance found **")

    def do_all(self, class_name):
        """ Print all string representations of instances """
        all_list = []
        if not class_name:
            for obj in HBNBCommand.objs.keys():
                all_list.append(str(HBNBCommand.objs[obj]))
            print(all_list)
            return
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        for obj in HBNBCommand.objs.keys():
            cls_name, id = obj.split(".")
            if cls_name == class_name:
                all_list.append(str(HBNBCommand.objs[obj]))
        print(all_list)

    def do_update(self, line):
        """ Updating attributes """
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
        id_search = 0
        for obj in HBNBCommand.objs.keys():
            cls_name, id = obj.split(".")
            if cls_name == list_args[0] and id == list_args[1]:
                inst = HBNBCommand.objs[obj]
                id_search = 1
                break
        if id_search == 0:
            print("** no instance found **")
            return
        if len(list_args) < 3:
            print("** attribute name missing **")
            return
        if len(list_args) < 4:
            print("** value missing **")
            return
        setattr(inst, list_args[2], list_args[3])
        inst.save()

    def default(self, line):
        """ Default commands """
        all_list = []
        count = 0
        list_args = line.split(".")
        for class_name in HBNBCommand.classes:
            if line == class_name + ".all()":
                for obj in HBNBCommand.objs.keys():
                    cls_name, id = obj.split(".")
                    if cls_name == class_name:
                        all_list.append(str(HBNBCommand.objs[obj]))
                print(all_list)
                return
            if line == class_name + ".count()":
                for obj in HBNBCommand.objs.keys():
                    cls_name, id = obj.split(".")
                    if cls_name == class_name:
                        count += 1
                print(count)
                return
            if len(list_args) > 1:
                if list_args[1][0:4] == "show":
                    inst_id = list_args[1][6:-2]
                    for obj in HBNBCommand.objs.keys():
                        cls_name, id = obj.split(".")
                        if cls_name == list_args[0] and id == inst_id:
                            print(HBNBCommand.objs[obj])
                            return
                    print("** no instance found **")
                    return
                if list_args[1][0:7] == "destroy":
                    inst_id = list_args[1][9:-2]
                    for obj in HBNBCommand.objs.keys():
                        cls_name, id = obj.split(".")
                        if cls_name == list_args[0] and id == inst_id:
                            del HBNBCommand.objs[obj]
                            models.storage.save()
                            return
                    print("** no instance found **")
                    return
                if list_args[1][0:6] == "update":
                    update_args = list_args[1].split(", ")
                    inst_id = update_args[0][8:-1]
                    if len(inst_id) == 0:
                        print("** instance id missing **")
                        return
                    if len(update_args) < 2:
                        print("** attribute name missing **")
                        return
                    if len(update_args) < 3 and update_args[1][0] != '{':
                        print("** value missing **")
                        return
                    class_name = list_args[0]
                    id_search = 0
                    for obj in HBNBCommand.objs.keys():
                        cls_name, id = obj.split(".")
                        if cls_name == class_name and id == inst_id:
                            inst = HBNBCommand.objs[obj]
                            id_search = 1
                            break
                    if id_search == 0:
                        print("** no instance found **")
                        return
                    if update_args[1][0] != '{':
                        setattr(inst, update_args[1][1:-1],
                                update_args[2][1:-2])
                    else:
                        for i in range(1, len(update_args)):
                            key, value = update_args[i].split(":")
                            if i == 1:
                                if len(update_args) > 2:
                                    setattr(inst, key[2:-1], value[2:-1])
                                if len(update_args) == 2:
                                    setattr(inst, key[2:-1], value[2:-3])
                            else:
                                if i == len(update_args) - 1\
                                   and len(update_args) > 2:
                                    setattr(inst, key[1:-1], value[1:-2])
                                if i > 1 and i < len(update_args) - 1:
                                    setattr(inst, key[1:-1], value[2:-1])
                    inst.save()
                    return
        print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
