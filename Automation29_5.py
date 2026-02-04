# Write a program which accepts a file name and one string from user and returns the frequency(count of occurrences) of that string in the file.

import sys

def main():
    FileName=sys.argv[1]
    String=sys.argv[2]

    f1=open(FileName,"r")
    Data=f1.read()
    f1.close()

    count=Data.count(String)
    print("Frequency of string is :",count)

if __name__=="__main__":
    main()