import sys

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
    target_directory = sys.argv[1]
    ignored_files = sys.argv[3:]

    files = aggergate_files(target_directory, ignored_files)
    with open(output_file, 'w') as output:
        for f in files:
            content = read_file(f)
            output.write(f"Content of {f}:\n{content}\n\n")


if __name__ == "__main__":
    main()
