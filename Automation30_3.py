# Write a program which accepts a file name from the user and display the contents of the file line by line on the screen.

import sys

def main():
    FileName=sys.argv[1]
    f1=open(FileName,"r")

    print("Display the contents of file :")
    for line in f1:
        print(line,end="")

    f1.close()


if __name__=="__main__":
    main()