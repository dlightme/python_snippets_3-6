# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 11:26:14 2021

@author: Whiskey Hotel

Convert Grid Reference to Quarter Tile format


"""
import sys

sGridRef = "TQ 26607 87334"
lGridRef = sGridRef.split( )   # split at space

tile = lGridRef[0]

easting = lGridRef[1][0]
northing = lGridRef[2][0]


#print ('debug E & N : ', easting, northing)
#print('debug, Quads: ', lGridRef[1][1], lGridRef[2][1])

def cardinalN (lGridRef):
    cCoord = int(lGridRef[2][1])
    
    if cCoord < 5:
        return "S"
    else:
        return "N"
    
def cardinalE (lGridRef):
    cCoord = int(lGridRef[1][1])
    
    if cCoord < 5:
        return "W"
    else:
        return "E"

print(sGridRef)
print(tile+easting+northing+cardinalN(lGridRef)+cardinalE(lGridRef))
#print(cardinalE(quadEast))