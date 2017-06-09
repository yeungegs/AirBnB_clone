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
    def do_show(self, arg):OB
        """
        Prints string representation of an instance
        based on the class name and id.
If the instance doesn't exist for the id, print ** no instance found **
If the id is missing, print ** instance id missing **
If the class name doesn't exist, print ** class doesn't exist **
If the class name is missing, print ** class name missing **
        """

    def do_destroy():
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        If the instance doesn't exist for the id, print ** no instance found **
        If the id is missing, print ** instance id missing **
        If the class name doesn't exist, print ** class doesn't exist **
        If the class name is missing, print ** class name missing **        
        """

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
        
