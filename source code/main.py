import os
from math import log10

files=os.listdir(".")

files.sort(key=lambda x: os.path.getmtime(x))
# print(files) # list index 0 hold the oldest file
digits=int(log10(len(files)))+1

for i in range(1,len(files)):
    newfile_name=f"{str(i).zfill(digits)}_{files[i]}"
    os.rename(files[i],newfile_name)
    # print(newfile_name)
