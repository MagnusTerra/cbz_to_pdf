import os

def get_file_directory(file_path):
    # Get the directory of the file
    directory = os.path.dirname(file_path)
    
    # Get the base folder name
    folder_name = os.path.basename(directory)
    
    return folder_name

# Example usage
file_path = '/home/user/cbz_to_pdf/test/Rakuen Translations , Taikutsu_Capítulo 60.10.cbz'
folder_name = get_file_directory(file_path)
print(f"The file is in the '{folder_name}' folder.")
