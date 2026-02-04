# Design automation script which accepts directory name and file extention from user.
# Display all files with that extention
# Usage : DirectoryFileSearch.py "Demo"."txt"

import os
import sys

def Accept():
    folder=sys.argv[1]
    ext=sys.argv[2]
    
    return folder,ext

def Display(folder,ext):
    files=os.listdir(folder)

    for f in files:
        if f.endswith("."+ext):
            print(f)
    print("All files with that extension are diplayed")

def main():
    folder,ext=Accept()
    Display(folder,ext)

if __name__=="__main__":
    main()