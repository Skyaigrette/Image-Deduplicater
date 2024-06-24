from cloner import clone_files
from duplicate_manager import get_files_to_delete
from file_manager import delete_given_path_list, create_folder
from win32com.client import Dispatch

def deduplicate(main_dir, clone_path = None):
    main_dir = main_dir

    if(clone_path == None):
        clone_dir = main_dir + "\\cloned_files"

    else:
        clone_path = clone_path # Where the files will be cloned?
    
    try:
        create_folder(clone_dir, True) # True -> The file will be hidden when it's created. 
    except:
        raise ValueError("Make sure you givven correct for clone folder.")

    
    clone_files(main_dir, clone_dir)

    files_to_delete =   get_files_to_delete(clone_dir)

    with open("bruh.txt", "w", encoding="UTF-8") as f:
        f.write(str(files_to_delete))
        f.close()

    delete_given_path_list(files_to_delete)
    delete_given_path_list([clone_dir])

if __name__ == '__main__':
    deduplicate("D:\\Yedekler")


