# Design automation script which accepts directory name and display checksum of all files.
# Usage : DirectoryChecksum.py "Demo"

import hashlib
import os

def CalculateChecksum(FileName):
    fobj=open(FileName,"rb")

    hobj=hashlib.md5()

    Buffer=fobj.read(1000) # Reads 1000 bytes of the file at a time

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1000)

    fobj.close()

    return hobj.hexdigest() # Returns the final checksum (a long string of letters and numbers)

def DirectoryWatcher(DirectoryName="Demo"):
    Ret=False

    Ret=os.path.exists(DirectoryName)
    if(Ret==False):
        print("There is no such directory")
        print("There is no such directory")
        return
    
    Ret=os.path.isdir(DirectoryName)
    if(Ret==False):
        print("It is not a directory")
        return

    for FolderName, SubfolderName, FileName in os.walk(DirectoryName): # os.walk goes through main folder,subfolder,files 
        for fname in FileName:
            fname=os.path.join(FolderName,fname) # Creates the full path of the file
            Checksum=CalculateChecksum(fname)

            print(f"File name :{fname} Checksum : {Checksum}")

def main():
    DirectoryWatcher()
if __name__=="__main__":
    main()
