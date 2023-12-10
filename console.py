#!/usr/bin/python3
""" console.py contains the entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit """
        return True

    def help_quit(self):
        """Help message for quit"""
        print("Quit command to exit the program")
        print("")

    def help_EOF(self):
        """Help message for EOF"""
        print("command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
