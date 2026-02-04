# Write a program which accepts a file name from the user and counts the total no of words in that file.

import sys

def main():
    FileName=sys.argv[1]

    f1=open(FileName,"r")
    content=f1.read()
    words=content.split()

    print("Number of words :",len(words))

if __name__=="__main__":
    main()