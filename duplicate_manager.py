import json
from imagededup.methods import CNN,PHash
from file_manager import get_file_id

def get_files_to_delete(files_path):
    path_data_file = open("files.json", "r")
    
    paths = json.load(path_data_file)
    
    files_to_remove = []

    method = PHash()

    encodings =  method.encode_images(image_dir=files_path)

    print("encoded")

    duplicates = method.find_duplicates_to_remove(encoding_map=encodings)
    
    print("dups found!")

    for duplicate in duplicates:
        path = paths[get_file_id(duplicate)]
        files_to_remove.append(path)
    
    print("list ready")

    path_data_file.close()

    return files_to_remove
