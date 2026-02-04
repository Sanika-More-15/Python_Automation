# Write a program which accepts a file name from the user, opens that file, and display the entire contents on the console.

import os

def main():
    FileName=input("Enter the name of file :")
    Ret=os.path.exists(FileName)

    if Ret==True:
        fobj=open(FileName,"r")
        print("The file gets successfully opened")
        print("File contents are:")
        print(fobj.read())
        fobj.close()
    else:
        print("File does not exits")


if __name__=="__main__":
    main()