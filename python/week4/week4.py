def read_file(file):
    """Read file from user"""
    try:
        with open(file, "r") as opened_file:
            content = opened_file.read()
            modified = content + "MODIFIED"
            return modified
    except FileNotFoundError:
        print("File does not exist")
    finally:
        print("Done reading")


def write_file(modified_content):
    """Write modified version into another file"""
    with open("modified.txt", "w") as write_file:
        write_file.write(modified_content)

file = input("What file do you wish to read?: ")
modified = read_file(file)
write_file(modified)
print("Modified file has been successfully written")
