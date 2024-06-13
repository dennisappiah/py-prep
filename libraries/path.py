"""
The os module represents paths as strings with which you cannot do much.
The pathlib module represents paths as special objects with useful methods and attributes.
"""
import os
from pathlib import Path

# prints current working directory path (C:\Users\denni\Videos\playingwithfiles)
cwd_path = Path.cwd()
print(cwd_path)

# change directory to Videos path
video_path = Path(r"C:\Users\denni\Videos")
print(video_path)

# access the parent directory path of the current directory  (C:\Users\denni\Videos)
parent_dir_path = cwd_path.parent
print(parent_dir_path)

# access the parent-parent directory path of the current directory (C:\Users\denni)
parent_parent_dir_path = cwd_path.parent.parent
print(parent_parent_dir_path)

# create directory in the current working directory path
Path("exampleDemo").mkdir(exist_ok=True)

"""same as"""
# if not os.path.exists("exampleDemo"):
#     os.mkdir("exampleDemo")

# Showing directory content (# os.listdir(‘example_data’))

total_size = 0
for path in Path("exampleDemo").iterdir():
    total_size = total_size + path.stat().st_size
    print(path.name, path.suffix, path.stat().st_size)
print(total_size)


"""
.exists(). This method checks if a file exists on the filesystem
print(video_path.exists())

.is_dir(). This method checks if the path represents a dictionary.
.is_file(). This method checks if the path represents a file.
.is_absolute(). This method checks if the path is an absolute path.
.chmod(). Change the file mode and permissions.
.is_mount(). Checks if the path is a mount point.
.suffix. Get the file extension (such as .jpeg, .png, or .pdf)
"""
