# Write a program which accepts a file name from the user and checks whether that file exists in the currents directory or not.

import os

def main():
    FileName=input("Enter the File Name :")

    if os.path.exists(FileName):
        print("File exists in current directory")
    else:
        print("File does not exists in current directory")

if __name__=="__main__":
    main()