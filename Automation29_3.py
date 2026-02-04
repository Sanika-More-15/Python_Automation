# Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt

import sys
import os

def main():
    source=sys.argv[1]
    destination=sys.argv[2]

    f1=open(source,"r")
    f2=open(destination,"a")

    f2.write(f1.read())

    f1.close()
    f2.close()

    print("File contents are copied Successfully")

if __name__=="__main__":
    main()