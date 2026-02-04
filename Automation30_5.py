# Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.

import sys

def main():
    FileName=sys.argv[1]
    word=sys.argv[2]

    f1=open(FileName,"r")
    Data=f1.read()
    f1.close()

    if word in Data:
        print("The word is present in file")
    else:
        print("The word is not present in file")


if __name__=="__main__":
    main()