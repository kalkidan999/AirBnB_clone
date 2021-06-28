#!/usr/bin/python3
""" 
contains the entry point of the command interpreter
"""
import cmd
import os
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ a command line interpreter """
    def do_quit(self, s):
        """ exit operation """
        return True

    def do_EOF(self, s):
        """ exit operation """
        return True

    def emptyline(self):
        """ empty line + ENTER shouldn’t execute anything """
        return False

    def do_help(self):
        """ help prompt """
        print "(hbnb)"