import os
 
path="data"  
dirList=os.listdir(path)
orderedDirList=sorted(dirList)
i=0
for fname in orderedDirList:
    previous_name = path + "/" + fname
    new_name = path + "/%03d.jpg" % i
 
    os.rename(previous_name,new_name) 
    i+=1