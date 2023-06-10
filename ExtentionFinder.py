import os

folder_prefix = "Documents/recup_dir."  # Change it to your recup directory. Make sure it ends with recup_dir.
folder_count = 6500  # Number of recup directories you have

file_extensions = set() 

for i in range(1, folder_count+1):
    folder_name = folder_prefix + str(i)
    

    for root, dirs, files in os.walk(folder_name):
        for file in files:
            filename, extension = os.path.splitext(file)
            file_extensions.add(extension.lower())

for extension in file_extensions: # prints file extentions
    extension = extension.replace(".", "")
    print(f'"{extension}"')
