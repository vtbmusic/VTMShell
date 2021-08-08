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
from cmd import Cmd
from libs.time import time_


class VTMShell(Cmd):
    prompt = 'VTMShell> '
    intro = "Welcome! Type ? to list commands"
 
    def do_exit(self, inp):
        'exit the application. Shorthand: x q Ctrl-D.'
        print("Bye")
        return True

    def do_time(self, inp):
        'Get current system time'
        print("Time: ", time_.nowtime())

    def do_dir(self, arg):
        'syntax: dir path -- displaya list of files and directories'
        if not arg:
            print("\n".join(os.listdir(".")))
        elif os.path.exists(arg):
            print("\n".join(os.listdir(arg)))
        else:
            print("No such pathexists.")
    
    def do_ls(self, arg):
        'syntax: dir path -- displaya list of files and directories'
        self.do_dir(arg)

    def do_clear(self, inp):
        
        pass
 
    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
 
        print("Default: {}".format(inp))
 
if __name__ == '__main__':
    VTMShell().cmdloop()