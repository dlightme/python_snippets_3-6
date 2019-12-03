# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:07:29 2019

@author: rockhunter
"""

list = ["1541_154_72_01","1541_154_72_00", "1541_154_72_03", "1541_154_82_01" ]
#print (len(list))

#print ("Print list [0], ", len(list),  list[0])
b = sorted(list)
#print ("Print Sorted[0], ", len(b), b[0])
#print (b)

for i in range(len(b)):
    print (b[i])

for elements in b:
    print (elements.split("_"))

for elements in b:
    #noofdashes = b[0].count("_")
    #print (noofdashes)
    ids = elements.split("_")
    print (ids[-2])
