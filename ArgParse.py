# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:00:56 2018

@author: whiskey hotel
"""
import argparse

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-p', action="store", type=str, dest="p", required=True)  #path
parser.add_argument('-n', action="store", type=str, dest="n", default="Auto_Unknown") #collection name
parser.add_argument('-t', action="store", type=int, dest="t", default=7) #image type
parser.add_argument('-r', action="store", type=int, dest="r", default=0) #image revision
parser.add_argument('-f', action="store", type=str, dest="f", default="tif") #filetype tif, jpg, etc.
print (parser.parse_args())

args = parser.parse_args()
print (args.p)


# =============================================================================
# 
# parser.add_argument('-a', action="store", type=int)
# parser.add_argument('-b', action="store", type=int)
# parser.add_argument('-c', action="store", type=int)
# print (parser.parse_args(['-a', '-b', '-c']))
# 
# =============================================================================
