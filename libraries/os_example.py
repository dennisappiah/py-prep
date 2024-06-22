"""
The os module represents paths as strings with which you cannot do much.
The pathlib module represents paths as special objects with useful methods and attributes.
"""

import os
from datetime import datetime


# change current working directory
os.chdir(r"C:\Users\denni\Videos")

# prints current working directory path
print(os.getcwd())

os.makedirs("OS-Demo2")

os.rename("OS-Demo2", "OS-Demo")


mod_time = os.stat("OS-Demo").st_mtime
print(datetime.fromtimestamp(mod_time))


# prints list of files and directories in current directory
print(os.listdir())

# walk or traverse through an entire directory tree
for dirpath, dirnames, filenames in os.walk(r"C:\Users\denni\Videos"):
    print("current Path", dirpath)
    print("Directories", dirnames)
    print("files", filenames)
    print()

# print path to home directory
print(os.environ.get("HOME"))

# joining path  (Os.path)
file_path = os.path.join(os.getcwd(), "text.tx")

print(os.path.basename(r"C:\Users\denni\Videos\text.txt"))  # returns `text.txt`
print(
    os.path.split(r"C:\Users\denni\Videos\text.txt")
)  # returns a tuple of  ('videos','text.txt)
print(
    os.path.splitext(r"C:\Users\denni\Videos\text.txt")
)  # returns ('videos\text', '.txt')
