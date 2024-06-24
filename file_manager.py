import os
import shutil
from win32com.client import Dispatch

def get_file_type(file_name):
    try:
        dot_index = file_name.rindex(".") + 1
    except ValueError:  # Daha spesifik bir istisna yakalamak
        return "NONE"
    return file_name[dot_index:]

def get_file_name_without_type(file_name):
    file_type = "." + get_file_type(file_name)
    return file_name.replace(file_type, "")

def get_file_id(file_name):
    file_name_raw = get_file_name_without_type(file_name)
    index = file_name_raw.rindex("_") + 1
    return file_name_raw[index:]

def copy_and_rename(src_path, dest_path, new_name):
    dest_full_path = os.path.join(dest_path, new_name)
    shutil.copyfile(src_path, dest_full_path)

# a list
def delete_given_path_list(path):
    for file_path in path:
        try:
            os.remove(file_path)
        except:
            print("Error during deleting this file => " + file_path)

def create_folder(folder_path, hidden=False):
    try:
        os.makedirs(folder_path)
    except:
        raise RuntimeError("Problem during creating folder: There might be another folder with same name.")
    if hidden:
        os.system(f'attrib +h "{folder_path}"')
