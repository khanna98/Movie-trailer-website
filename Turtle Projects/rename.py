# Get all the filenames. DONE :)
# Rename each file. 
import os
def rename_files():
		file_list = os.listdir(r"/home/mayank/Downloads/Compressed/prank/prank")
		#print(file_list)
		path = os.getcwd()
		change_path = os.chdir(r"/home/mayank/Downloads/Compressed/prank/prank")
		for file_name in file_list:
				os.rename(file_name,file_name.translate(None,"0123456789"))
		os.chdir(path)

rename_files()
