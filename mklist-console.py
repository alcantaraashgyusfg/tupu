import os

def list_files_in_folder(folder_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_list.append(file_name)
    return file_list

def main():
    folder_path = input("Enter the path of the folder: ")

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    file_list = list_files_in_folder(folder_path)

    print("Files in the folder:")
    for file_name in file_list:
        print(file_name)

if __name__ == "__main__":
    main()
