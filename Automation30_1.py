# Write a program which accepts a file name from the user and counts how many lines are present in the file.

import sys

def main():
    FileName=sys.argv[1]

    f1=open(FileName,"r")
    lines=f1.readlines()
    f1.close()

    print("Number of lines :",len(lines))

if __name__=="__main__":
    main()