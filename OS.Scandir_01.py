# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:42:41 2019

@author: rockhunter
"""
import os
path = "V:\\1541_Queens Square, Croydon - Rolfe Judd\\AVR-Output"

for entry in os.scandir(path):
   if not entry.name.startswith('.') and entry.is_dir():
       print(entry.name)