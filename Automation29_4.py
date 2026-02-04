# Write a program which accepts two file names through command line arguments and compare the contents of both files.

import sys
import os

def main():
    source=sys.argv[1]
    destination=sys.argv[2]

    f1=open(source,"r")
    f2=open(destination,"r")

    if f1.read() == f2.read():
        print("Both files are same ")
    else:
        print("Both files are different")

    f1.close()
    f2.close()

if __name__=="__main__":
    main()