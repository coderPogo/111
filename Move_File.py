import shutil
import os

from_dir = "/Users/pogo/Downloads"
to_dir = "/Users/pogo/Document_Files"
list_of_files = os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
    root,extension = os.path.splitext(i)

    print("root of file name is:", root)
    print("extension of file name is:", extension)