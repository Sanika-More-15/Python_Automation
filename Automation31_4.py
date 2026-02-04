# Design automation script which accept two directory names and one file extention. 
# Copy all files with specified extention from first directory into second dirctory. 
# Second directory should be created at runtime 
# Usage : DirectoryCopy.py "Demo" "Temp" .ext

import os
import sys

def AcceptInput():
    src = sys.argv[1]
    dest = sys.argv[2]
    ext = sys.argv[3]      # example: .txt
    return src, dest, ext

def CreateDir(dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

def CopyFiles(src, dest, ext):
    for file in os.listdir(src):

        # copy ONLY matching extension files
        if file.endswith(ext):
            src_file = os.path.join(src, file)
            dest_file = os.path.join(dest, file)

            if os.path.isfile(src_file):
                f1 = open(src_file, "rb")
                data = f1.read()
                f1.close()

                f2 = open(dest_file, "wb")
                f2.write(data)
                f2.close()

    print("Selected files copied successfully")

def main():
    src, dest, ext = AcceptInput()
    CreateDir(dest)
    CopyFiles(src, dest, ext)

if __name__ == "__main__":
    main()
