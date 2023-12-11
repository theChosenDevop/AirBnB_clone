#!/usr/bin/python3
"""Defines HBnB console"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb )"
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def do_quit(self, arg):
        """quit the command line interepreter """
        return True

    def do_EOF(self, arg):
        """quit on EOF"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")
        print("")

    def help_EOF(self):
        """Help message for EOF command"""
        print("EOF command to exit the program")

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        """
    if not arg:
        print("** class name missing **")
    elif arg not in HBNBCommand.classes:
        print("** class doesn't exist **")
    else:
        new_instance = BaseModel()
        new_instance.save()


if __name__ == "__main__":
    HBNBCommand.cmdloop()
