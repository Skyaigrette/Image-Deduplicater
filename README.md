 This code will deduplicate your images in a folder. It doesn't only check your given folder, it also checks subfolders.

1. Cloning: First, all files will be copied into another folder because, as I understand, you can't search multiple folders with the imagededup library.
2. Saving File Data: During the cloning process, every image file will get an ID, and a dictionary will be generated. In this dictionary, you can find the real path of an image file. After the dictionary has been created, it will be saved as a JSON file. Cloned images' IDs are added to the last part of the cloned file name. For example, if you have a "C.jpg" file, it will be cloned as "C_132.jpg" if the ID is 132.
3. Detecting: After the cloning process is done, the imagededup library will detect the duplicated files and determine which files will be deleted. Then, those file paths will be saved in a list with their IDs.
4. Deleting: In the last part, via this list, all the duplicated files and the clone folder will be deleted.

This code was tested with nearly 16,500 image files and it worked well. If you encounter any problems or have an idea to develop this project, don't hesitate to reach me.
