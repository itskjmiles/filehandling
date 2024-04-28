import os

def count_file_extensions(directory):
    try:
        extension_count = {}

        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                _, extension = os.path.splitext(filename)
                extension = extension.lower() 

                extension_count[extension] = extension_count.get(extension, 0) + 1

        for extension, count in extension_count.items():
            print(f"{extension[1:]}: {count}") 
    except FileNotFoundError:
        print("Directory not found.")
    except PermissionError:
        print("Permission denied.")

directory_path = input("Enter the directory path: ")

count_file_extensions(directory_path)
