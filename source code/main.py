import os
from math import log10

files=os.listdir(".")

files.sort(key=lambda x: os.path.getmtime(x))
# print(files) # list index 0 hold the oldest file
digits=int(log10(len(files)))+1

print(f"Please note: Hidden files lead to non-consecutive renaming sometimes. Move or delete files/folder if anyone start with '.' to gain consecutive naming. \nor you can proceed anyway? ('y'/'Y' or any key to quit)")
n=input()

if(n=="y" or n=="Y"):
    rename=0
    for i in range(len(files)-1):
        if(files[i][0]=="."):
            rename-=1
            continue

        if "_" in files[i] and files[i][0]!="_":
            index=files[i].find("_")
            isNum=files[index-1]
        
            if(isNum >="0" and isNum<="9"):
                oldName=files[i][index+1:]
            else:
                oldName=files[i]
        else:
            oldName=files[i]

        rename+=1
        newfile_name=f"{str(rename).zfill(digits)}_{oldName}"

        os.rename(oldName,newfile_name)
        # print(newfile_name)
        # print(oldName)
else:
    print("File renaming cancel.")
    exit(0)