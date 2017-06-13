#!/usr/bin/python3
"""
This is module test_console.
This module is a unittest for the console module.
it can be run with `python -m unittest tests/test_console.py`
"""
import unittest
import sys
from unittest.mock import patch
from io import StringIO
import console


class TestConsole(unittest.TestCase):
    """
    This class is a unittest for the console module

    **Instance methods**
    """
    def setUp(self):
        """Redirects stdin and stdout"""
        self.command = console.HBNBCommand()

    def test_help(self):
        """
        Tests the help command
        """
        with patch('sys.stdout', new=StringIO()) as test_out:
            self.assertFalse(self.command.onecmd("help"))
            
    def test_quit(self):
        pass

    def test_EOF(self):
        pass

if __name__ == "__main__":
    unittest.main()
