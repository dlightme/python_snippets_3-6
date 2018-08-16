# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:00:56 2018

@author: whiskey hotel
"""
import argparse

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-p', action="store", type=str, default="%appdata%")
parser.add_argument('-n', action="store", type=str, default="Auto_Unknown")
parser.add_argument('-t', action="store", type=int, default=7)
parser.add_argument('-r', action="store", type=int, default=0)
parser.add_argument('-f', action="store", type=str, default="tif")
print (parser.parse_args())



# =============================================================================
# 
# parser.add_argument('-a', action="store", type=int)
# parser.add_argument('-b', action="store", type=int)
# parser.add_argument('-c', action="store", type=int)
# print (parser.parse_args(['-a', '-b', '-c']))
# 
# =============================================================================
