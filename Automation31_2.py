# Design automation script which accepts directory name and two file extention from user.
# Rename all files with first file extention with the second file extention
# Usage : DirectoryFileSearch.py "Demo"."txt"

import os
import sys

def Accept():
    folder=sys.argv[1]
    ext1=sys.argv[2]
    ext2=sys.argv[3]
    return folder,ext1,ext2

def Rename_ext(folder,old_ext,new_ext):

    files=os.listdir(folder)
    
    for f in files:
        if f.endswith("."+old_ext):
            old_name=os.path.join(folder,f)
            new_name=os.path.join(folder,f.replace("."+old_ext,"."+new_ext))
            os.rename(old_name,new_name)
    
    print("Your file is renamed")

def main():
    folder,ext1,ext2=Accept()
    Rename_ext(folder,ext1,ext2)

if __name__=="__main__":
    main()