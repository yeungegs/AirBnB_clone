#!/usr/bin/python3
"""
this module contains the entry point of the command interpreter
"""
import cmd
import sys
from models.base_model import BaseModel

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
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel 
        saves it (to the JSON file) and prints id.
        If the class name doesn't exist, print ** class doesn't exist **
        If the class name is missing, print ** class name missing **
        """
        if arg and arg in HBNBCommand.myClasses.keys():
            newBase = HBNBCommand.myClasses[arg]()
            newBase.save()
            print(newBase.id)
        elif not arg:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

        
    def do_show(self, args):
        """
        Prints string representation of an instance
        based on the class name and id.
        If the instance doesn't exist for the id, print ** no instance found **
        If the id is missing, print ** instance id missing **
        If the class name doesn't exist, print ** class doesn't exist **
        If the class name is missing, print ** class name missing **
        """
        print(type(args))
        if args:
            args = [x.strip() for x in args.split()]
            print(args)
        if len(args) == 2:
            if args[0] in HBNBCommand.myClasses.keys():
                result = "{}.{}".format(args[0], args[1])
                if result in storage.all().keys():
                    print(storage.all()[result])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            print("** class name missing **")


    def do_destroy():
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        If the instance doesn't exist for the id, print ** no instance found **
        If the id is missing, print ** instance id missing **
        If the class name doesn't exist, print ** class doesn't exist **
        If the class name is missing, print ** class name missing **        
        """
        if len(args) == 2:
            if args[0] in HBNBCommand.myClasses:
                myInstance = "{}.{}".format(args[0], args[1])
                if myInstance in storage.all().keys():
                    del storage.all()[result]
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 1 and args[0]:
            print("** instance id missing **")
        else:
            print("** class name missing 

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the class name.
        If the class name doesn't exist, print ** class doesn't exist **
        """
        

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        
        If the instance doesn't exist for the id, print ** no instance found **
        If the id is missing, print ** instance id missing **
        If the class name doesn't exist, print ** class doesn't exist **
        If the class name is missing, print ** class name missing **
        If the attribute name is missing, print ** attribute name missing **
        If the value for the attribute name doesn't exist, print ** value missing **

        """
        
