import sys
import os
from gpt import prompt_gpt


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
    if len(sys.argv) != 2:
        print("Usage: codemapai <directory> --ignore <filename1> <filename2> ... <filenameN>")
        sys.exit(1)

    target_directory = sys.argv[1]
    ignored_files = sys.argv[3:]

    # Prompt user to pick diagram type
    print("Diagram Options:")
    print("1: System diagram")
    print("2: File diagram")
    diagram_type = ""
    flag = True
    while flag:
        diagram_type = input("What type of diagram would you like: ")

        if diagram_type not in ['1','2']:
            print("Invalid choice. Please enter 1 or 2.")
        else:
            flag = False

    files = aggregate_files(target_directory, ignored_files)
    combined_content = ""
    for f in files:
        content = read_file(os.path.join(target_directory, f))
        combined_content += f"Content of {os.path.join(target_directory, f)}:\n{content}\n\n"

    # print(combined_content)

    # TODO: Call the gpt.py here
    prompt_gpt(combined_content)
        


if __name__ == "__main__":
    main()
