"""Automate parsing and renaming of files in a directory"""

import os

os.chdir(r"C:\Users\kofid\Videos")


for file in os.listdir():
    # print(file)
    filename, ext = os.path.splitext(file)  # returns a tuple of filename and ext
    f_title, f_course, f_num = filename.split("-")

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:]

    new_name = f"{f_num}-{f_title}{ext}"

    os.rename(file, new_name)
