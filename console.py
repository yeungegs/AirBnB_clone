#!/usr/bin/python3
import cmd
"""
this module contains the entry point of the command interpreter
"""

class HBNBCommand(cmd.Cmd):
    """
    this module contains one class: `HBNBCommand()`
    """
    prompt = "(hbnb) "
    obj = models.storage.all()
    def quit(self, arg):
        """Quit command to exit the program"""
        self.close()
        bye()
        return True 
    def do_EOF(self, line):
        """Exit the program
        """
        return True
