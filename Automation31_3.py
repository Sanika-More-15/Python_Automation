# Design automation script which accept two directory names. Copy all files from first directory into second dirctory. Second directory should be created at runtime
# Usage : DirectoryCopy.py "Demo" "Temp"

import os
import sys

def AcceptInput():
    src=sys.argv[1]
    dest=sys.argv[2]
    return src,dest

def CreatDir(dest):
    if not os.path.exists(dest):
        os.mkdir(dest)   # The os.mkdir() method is used to create a directory.

def CopyFiles(src,dest):
    for file in os.listdir(src):
        src_file=os.path.join(src,file)
        dest_file=os.path.join(dest,file)

        if os.path.isfile(src_file):
            f1=open(src_file,"rb")
            data=f1.read()
            f1.close()

            f2=open(dest_file,"wb")
            f2.write(data)
            f2.close()
    print("All files from 1st Directory is copied into 2nd Directory.")

def main():
    src,dest=AcceptInput()
    CreatDir(dest)
    CopyFiles(src,dest)

if __name__=="__main__":
    main()