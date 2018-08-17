# -*- coding: utf-8 -*-
"""
Spyder Editor
Author: Whiskey Hotel
Pyhton 3.6.x
"""
import os
import re
import sys
import argparse

parser = argparse.ArgumentParser(description='Adobe Bridge Collections Generator')

parser.add_argument('-p', action="store", type=str, dest="p", required=True)  #path
parser.add_argument('-n', action="store", type=str, dest="n", default="Auto_Unknown") #collection name
parser.add_argument('-t', action="store", type=int, dest="t", default=7) #image type
parser.add_argument('-r', action="store", type=int, dest="r", default=0) #image revision
parser.add_argument('-f', action="store", type=str, dest="f", default="tif") #filetype tif, jpg, etc.

args = parser.parse_args()

# =============================================================================
# Adobe boilerplate definitions
# =============================================================================
    
header1 ="<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>\n" 
header2 ="<arbitrary_collection version='1'>\n"
prefix = "\t<file uri='bridge:fs:file:///" #\t add tab \n adds carraige return
appendix = "'>\n"
footer ="</arbitrary_collection>"    

# =============================================================================
# Contruct RegEx for File Search
# =============================================================================
def RegConstr():
    imageType = str(args.t)
    imageRev = str(args.r)
    imageFile = args.f
    RegStr = "\d{4}[_]\d{3}[_][" + imageType +"][" + imageRev + "][_]\d{2}\." + imageFile
    print (RegStr)
    return RegStr
    #\d{4}[_]\d{3}[_][7\d]{2}[_]\d{2}\.(tif)
    
insert = RegConstr()

# =============================================================================
# RegEx Matching Stuff
# =============================================================================
matches = []
img_re = re.compile(insert, re.IGNORECASE)

try:
    for root, dirnames, filenames in os.walk(args.p):
        matches.extend(os.path.join(root, name) for name in filenames if img_re.match(name))
except:
    print >> sys.stderr, "Path Error, directory not found"
    sys.exit(1)
    
def outputf(filelst):
    bridgelst = [s.replace('\\', '/') for s in filelst]
    bridgelst = [s.replace(' ', '%20') for s in bridgelst]
    return bridgelst

try:
    outputfile = "C:/Users/rockhunter/AppData/Roaming/Adobe/Bridge CC 2018/Collections/Auto_" + args.n + ".filelist"
except:
    print("Something Wrong with output path")
    sys.exit(1)
    
try:
    with open(outputfile, "w") as f:
        f.write(header1) 
        f.write(header2)
        for n in outputf(matches):
            f.write(prefix + n + appendix) #sorry this is messy
        f.write(footer)
except:
    print("Something Wrong with writing to file")
    sys.exit(1)    

def main():
    print("Program End, Probably Successful, check %appdata")

if __name__ == '__main__':
    main()