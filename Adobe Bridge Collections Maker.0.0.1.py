# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import re

header1 ="<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>\n" 
header2 ="<arbitrary_collection version='1'>\n"
prefix = "\t<file uri='bridge:fs:file:///" #\t add tab \n adds carraige return
appendix = "'>\n"
footer ="</arbitrary_collection>"    


matches = []
#\d{4}[_]\d{3}[_][W\d]{2}[_]\d{2}.tif
# img_re = re.compile(r'.+\.(psd)$', re.IGNORECASE)
img_re = re.compile(r'\d{4}[_]\d{3}[_][7\d]{2}[_]\d{2}\.(tif)$', re.IGNORECASE) #dddd_ddd_7d_dd.tif

for root, dirnames, filenames in os.walk(r"V:\1525_Hornsey Town Hall Planning"):
    matches.extend(os.path.join(root, name) for name in filenames if img_re.match(name))

def outputf(filelst):
    bridgelst = [s.replace('\\', '/') for s in filelst]
    bridgelst = [s.replace(' ', '%20') for s in bridgelst]
    return bridgelst

with open("C:/Users/rockhunter/AppData/Roaming/Adobe/Bridge CC 2018/Collections/Auto_1525_Hornsey Town Hall Planning.filelist", "w") as f:
    f.write(header1) 
    f.write(header2)
    for n in outputf(matches):
        f.write(prefix + n + appendix) #sorry this is messy
    f.write(footer)
        