import MaxPlus as MP
import pymxs

mySel = MP.SelectionManager.Nodes
objectList = []

for each in mySel:
    x = each.Name
    objectList.append(x)

print objectList

