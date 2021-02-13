#!/usr/bin/python3
import argparse
import os
from shutil import copyfile, move


class FileManager:
    @staticmethod
    def move_file(source_file: str, destination_file: str):
        """Moves a file from a source path to a destination path. Make sure that the destination already exists."""
        try:
            move(source_file, destination_file)
        except FileNotFoundError as e:
            print(f"Either {source_file} or {destination_file} could not be found!")
            print(f"Error {e}")

    @staticmethod
    def create_folder(folder_path: str = os.getcwd()) -> None:
        """Creates a folder in the specified path"""
        try:
            os.mkdir(folder_path)
        except OSError as e:
            print(f"Creation of {folder_path} Failed")
            print(f"Error {e}")
        else:
            print(f"Folder {folder_path} is created successfully")

    @staticmethod
    def create_file(file_name: str, folder_path: str = os.getcwd(),) -> None:
        """Creates a file. If the folder path is not specified then the apth of the current directory is used."""
        full_file_path = os.path.join(folder_path, file_name)
        # if it already exists it does not do anything
        with open(full_file_path, 'w'):
            pass

    @staticmethod
    def show_files_in_folder(directory_path: str):

        for root, dirs, files in os.walk(directory_path):
            for d in dirs:
                print(os.path.join(root, d))
            for f in files:
                print(os.path.join(root, f))

    @staticmethod
    def copy_file(source_path: str, destination_path: str):
        try:
            copyfile(source_path, destination_path)
        except OSError as e:
            print(f"File {source_path} could not be copied")
            print(f"Error {e}")
        else:
            print(f"File {source_path} is copied successfully")


def get_arguments():
    """Gets arguments and creates parser from terminal command."""
    try:
        parser = argparse.ArgumentParser(description="File Injector")

        parser.add_argument("--m", "--method", dest="method", help="Method to perform", type=str, required=True)
        parser.add_argument("--f", "--file_one", dest="file_one",
                            help="First argument that can be a folder's name, file's name or path", type=str)
        parser.add_argument("--s", "--file_two", dest="file_two",
                            help="Second argument that can be a folder's name, file's name or path", type=str)

        options = parser.parse_args()
        if not options.method:
            parser.error("[-]   Please specify a  method use --help for more")
        return options
    except AttributeError:
        os.system('clear')


def main():
    """Script entrypoint"""
    file_mng = FileManager()
    arguments = get_arguments()
    method = arguments.method

    argument_1 = None
    argument_2 = None

    if arguments.file_one:
        argument_1 = arguments.file_one
    if arguments.file_two:
        argument_2 = arguments.file_two

    if method == 'create_folder':
        file_mng.create_folder(argument_1)
    elif method == 'create_file':
        file_mng.create_file(argument_1, argument_2)
    elif method == 'show_files_in_folder':
        file_mng.show_files_in_folder(argument_1)
    elif method == 'move_file':
        file_mng.move_file(argument_1, argument_2)
    elif method == 'copy_file':
        file_mng.copy_file(argument_1, argument_2)
    else:
        print("[-] Method not supported")


if __name__ == '__main__':
    main()

