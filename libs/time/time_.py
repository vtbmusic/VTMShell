#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
	*************************** 
	--------description-------- 
 	 Autor: Kuro Kitu
 	 Description: Time Command
 	 Date: 2021-08-09 01:45:02
 	 LastEditors: Kuro Kitu
 	 LastEditTime: 2021-08-09 01:45:03

	***************************
"""

import time

def nowtime():
    return time.asctime( time.localtime(time.time()))