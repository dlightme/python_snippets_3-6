# -*- coding: utf-8 -*-
"""
Spyder Editor
Author: Wolfgang Haak
Pyhton 3.6.x
"""

import os
import re
import sys

def main():
    print("Program End, Probably Successful, check %appdata")

header1 ="<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>\n" 
header2 ="<arbitrary_collection version='1'>\n"
prefix = "\t<file uri='bridge:fs:file:///" #\t add tab \n adds carraige return
appendix = "'>\n"
footer ="</arbitrary_collection>"    

if len(sys.argv) != 3:
        print("Probably not the right number of arguments, try \"InputPath\" \"OutputName\"")
        sys.exit(1)

matches = []
#\d{4}[_]\d{3}[_][W\d]{2}[_]\d{2}.tif
# img_re = re.compile(r'.+\.(psd)$', re.IGNORECASE)
img_re = re.compile(r'\d{4}[_]\d{3}[_][7\d]{2}[_]\d{2}\.(tif)$', re.IGNORECASE) #dddd_ddd_7d_dd.tif

try:
    for root, dirnames, filenames in os.walk(sys.argv[1]):
        matches.extend(os.path.join(root, name) for name in filenames if img_re.match(name))
except:
    print >> sys.stderr, "Path Error, directory not found"
    sys.exit(1)
    
def outputf(filelst):
    bridgelst = [s.replace('\\', '/') for s in filelst]
    bridgelst = [s.replace(' ', '%20') for s in bridgelst]
    return bridgelst

try:
    outputfile = "C:/Users/rockhunter/AppData/Roaming/Adobe/Bridge CC 2018/Collections/Auto_" + sys.argv[2] + ".filelist"
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


if __name__ == '__main__':
    main()