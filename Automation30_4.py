# Write a program which accepts two file name from the user.
# First file is existing file
# Second file is a new file

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