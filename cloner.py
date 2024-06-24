import os
import json
from file_manager import get_file_type, get_file_name_without_type, copy_and_rename

filetypes = ["heic","HEIC","MOV","jpg","jpeg","png"]
files  = []

def clone_files(main_directory, copy_directory):
    file_dictionary = {}
    files_to_clone = []
    fileId = 0
    for root,dirs,files in os.walk(main_directory):
        print(files)
        print(dirs)
        print(root)
        for file in files:
            fileType = get_file_type(file)
            path = os.path.join(root, file)
            if(fileType in filetypes):
                fileId += 1 
                file_dictionary[fileId] = path
                files_to_clone.append([fileId, file, path])
            print(file + " -> " + path + " | " + str(fileId))

    for file_info in files_to_clone:
        file_id = file_info[0]
        file_name = file_info[1]
        file_path = file_info[2]
        file_type = get_file_type(file_name)
        file_copy_name = f"{get_file_name_without_type(file_name)}_{str(file_id)}.{file_type}"
        copy_and_rename(file_path, copy_directory, file_copy_name)
        
        print(f"{file_path} has been copied to this directory as {file_copy_name} | {file_id}\n\n")

    with open("files.json", "w", encoding="utf-8") as f:
        json.dump(file_dictionary, f)
        f.close()
