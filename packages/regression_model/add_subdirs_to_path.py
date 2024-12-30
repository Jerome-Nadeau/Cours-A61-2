import os
import sys

def add_parent_directory_to_path():
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(parent_dir)

def add_subdirectories_to_path(rootdir):
    for dirpath, dirnames, filenames in os.walk(rootdir):
        sys.path.append(dirpath)

rootdir = os.path.dirname(os.path.abspath(__file__))
add_parent_directory_to_path()
add_subdirectories_to_path(rootdir)
