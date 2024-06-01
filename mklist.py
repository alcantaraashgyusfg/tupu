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

    output_path = input("Enter the path where you want to save the output file (including file name and extension): ")

    with open(output_path, 'w') as output_file:
        for file_name in file_list:
            output_file.write(file_name + '\n')

    print(f"File names written to {output_path}.")

if __name__ == "__main__":
    main()
