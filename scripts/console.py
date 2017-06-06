#!/usr/bin/python3
"""Custom command line for AirBnB project
"""
import cmd



class HBNBCommand(cmd.Cmd):
    """ Command Line Interpreter Class """

    prompt = "(hbnb) "
    """    
    def __init__(self):
        cmd.Cmd = __init__.self
    """
    def do_prompt(self):
        """Custom prompt
        """
        self.prompt = line

    def do_EOF(self, line):
        """Exit
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """ Nothing """
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
