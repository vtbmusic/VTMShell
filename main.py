#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
	*************************** 
	--------description-------- 
 	 Autor: Kuro Kitu
 	 Description: VTM Shell Main
 	 Date: 2021-08-09 01:31:48
 	 LastEditors: Kuro Kitu
 	 LastEditTime: 2021-08-09 01:40:42

	***************************
"""

import os
import json
from os import *
from cmd import Cmd
from platform import version
from libs.time import *
from libs.clear import *
from libs.file import *

version = 1.0
config = None

class VTMShell(Cmd):
    prompt = '\033[0;32;40mVTMShell> \033[0m'
    intro = """
    \033[0;32m
     _    __________  ________ __         ____
    | |  / /_  __/  |/  / ___// /_  ___  / / /
    | | / / / / / /|_/ /\__ \/ __ \/ _ \/ / / 
    | |/ / / / / /  / /___/ / / / /  __/ / /  
    |___/ /_/ /_/  /_//____/_/ /_/\___/_/_/
    
    VTMShell V%s 
    Welcome! Type ? to list commands

    Now Time is %s

    \033[0m
    """ % (version, nowtime())

    def do_exit(self, inp):
        'exit: exit the application. Shorthand: x q Ctrl-D.'
        print("Bye")
        return True

    def do_time(self, inp):
        'time: Get current system time'
        print("Time: ", nowtime())

    def do_dir(self, arg):
        'die: syntax: dir path -- displaya list of files and directories'
        if not arg:
            print("\n".join(os.listdir(".")))
        elif os.path.exists(arg):
            print("\n".join(os.listdir(arg)))
        else:
            print("No such pathexists.")

    def do_ls(self, arg):
        'ls: syntax: dir path -- displaya list of files and directories'
        self.do_dir(arg)

    def do_clear(self, inp):
        'clear: Clear Screen'
        clear()

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)

        print("Default: {}".format(inp))


if __name__ == '__main__':
    config = json.loads(read_file('./configs/main.json'))
    print(type(config))
    if(config != None):
        clear()
        VTMShell().cmdloop()
