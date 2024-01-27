import sys
import os
from .gpt import


def read_file(file):
    """Helper function to read contents of an individual file."""
    with open(file, 'r') as f:
        file_content = f.read()
    return file_content


def aggregate_files(directory, ignore):
    """Function that goes through all the files in a directory."""
    file_list = []
    for root, subdirs, files in os.walk(directory):
        for f in files:
            path = os.path.relpath(os.path.join(root, f), directory)
            if path not in ignore:
                file_list.append(path)
    return file_list


def main():
    # TODO: Make sure the number of arguments is right
    # TODO: Remove the list of ignored files
    target_directory = sys.argv[1]
    ignored_files = sys.argv[3:]

    files = aggregate_files(target_directory, ignored_files)
    # print(files)
    with open("output.txt", 'w') as output:
        for f in files:
            content = read_file(os.path.join(target_directory, f))
            output.write(f"Content of {os.path.join(target_directory, f)}:\n{content}\n\n")

        # TODO: Call the gpt.py here
        


if __name__ == "__main__":
    main()
