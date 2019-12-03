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

parser = argparse.ArgumentParser(description='CSV Collector')

parser.add_argument('-p', action="store", type=str, dest="p", required=False, default="V:\\1541_Queens Square, Croydon - Rolfe Judd\\AVR-Output")  #path
#parser.add_argument('-n', action="store", type=str, dest="n", default="Auto_Unknown") #collection name
#parser.add_argument('-t', action="store", type=int, dest="t", default=7) #image type
parser.add_argument('-r', action="store", type=int, dest="r", default=2) #image revision
parser.add_argument('-f', action="store", type=str, dest="f", default="tif") #filetype tif, jpg, etc.

args = parser.parse_args()

# =============================================================================
# Contruct RegEx for File Search
# =============================================================================
def RegConstr():
#    imageType = str(args.t)
    imageRev = str(args.r)
    imageFile = args.f
    RegStr = "\d{4}[_]\d{3}[_][0578][" + imageRev + "][_]\d{2,3}\." + imageFile
    print (RegStr)
    return RegStr
    
    
insert = RegConstr()

# =============================================================================
# RegEx Matching Stuff
# =============================================================================
def walk(insert):
    matches = []
    img_re = re.compile(insert, re.IGNORECASE)
    
    try:
        for root, dirnames, filenames in os.walk(args.p):
            matches.extend(os.path.join(root, name) for name in filenames if img_re.match(name))
    except:
        print >> sys.stderr, "Path Error, directory not found"
        sys.exit(1)
    return matches
#    for e in matches:
#        print (e)

# =============================================================================
# Copy list and prune to latest result.
# =============================================================================

def walkdepth(startdir, depth):
    #print (root, root.count(os.sep))
    matches=[]
    for items in startdir:
        for root, dirnames, filenames in os.walk(startdir):
            if root.count(os.sep) - items.count(os.sep) > depth: #count the number of seperators and delete any that are larger than that
                del dirnames[:]                
            matches.extend(os.path.join(root, name) for name in dirnames)
    return matches

def walkdepth2(startdir, depth):
    matches =[]
    for root, dirnames, files in os.walk(startdir):
        if root[len(startdir):].count(os.sep) < depth:
            #for dir in dirnames:
            matches.extend(os.path.join(root, name) for name in dirnames)
    print (len(matches))
    return matches

#result = walk(insert)
startdir = args.p    
result = walkdepth2(startdir, 2)


lsorted = sorted(result)
print (len(result))
for i in lsorted:
    print (i)

# =============================================================================
# def outputf(filelst):
#     bridgelst = [s.replace('\\', '/') for s in filelst]
#     bridgelst = [s.replace(' ', '%20') for s in bridgelst]
#     return bridgelst
# =============================================================================

# =============================================================================
# try:
#     outputfile = "C:/Users/rockhunter/Documents" + args.n + ".csv"
# except:
#     print("Something Wrong with output path")
#     sys.exit(1)
#     
# try:
#     with open(outputfile, "w") as f:
#         for n in outputf(matches):
#             f.write(prefix + n + appendix) #sorry this is messy
#         
# except:
#     print("Something Wrong with writing to file")
#     sys.exit(1)    
# =============================================================================

def main():
    print("Program End, Probably Successful.")

if __name__ == '__main__':
    main()