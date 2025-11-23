

import os

# Define the directory where document files are stored
DOCS_DIR = "docs"
# Initialize a global variable to store the file path
PATH = ""

def read():
    """
    Reads the text in 'poem.txt' line by line and prints each line.
    """
    # Declare PATH as a global variable to modify it
    global PATH
    # Construct the full path to 'poem.txt'
    PATH = os.path.join(DOCS_DIR, "poem.txt")
    # Print the determined file path
    print(PATH)
    # Open the file in read mode ("r") using a 'with' statement for automatic closure
    with open(PATH, "r") as f:
        # Iterate over each line in the file
        for lines in f:
            # Print the line after removing leading/trailing whitespace and newline characters
            print(lines.strip().replace("\n", ""))


def reverse():
    """
    Reads the content of 'poem.txt', prints the lines in reverse order,
    and returns the reversed poem as a single string.
    """
    global PATH
    PATH = os.path.join(DOCS_DIR, "poem.txt")
    print(PATH)
    # Open the file in read mode ("r")
    with open(PATH, "r") as f:
        # Read all lines from the file into a list
        lines = f.readlines()

    # Iterate over the list of lines in reverse order
    for line in reversed(lines):
        # Print the reversed line after stripping whitespace and newlines
        print(line.strip().replace("\n", ""))

    # Reverse the list of lines and join them into a single string to return
    return "".join(reversed(lines))

def write():
    """
    Calls reverse() to get the reversed poem content and writes it to 'poem2.txt'.
    """
    global PATH
    PATH = os.path.join(DOCS_DIR, "poem2.txt")
    print(PATH)
    # Open the output file in write mode ("w")
    with open(PATH, "w") as f:
        # Call reverse() to get the reversed content and write it to the file
        f.write(reverse())

def append():
    """
    Appends a name and message to the end of the 'poem2.txt' file.
    """
    global PATH
    PATH = os.path.join(DOCS_DIR, "poem2.txt")
    with open(PATH, "a") as f:
        # Write the name line with newlines before and after
        f.write("\n My name is Rachel Feuchtwanger \n")
        # Write the message line with a trailing newline
        f.write("I like this poem because it is cute :) \n")


def main():
    """
    The main function that executes the file operations sequence:
    read -> reverse -> write -> append.
    """
    # Call the function to read and print the original poem
    read()
    # Call the function to read and print the poem in reverse order
    reverse()
    # Call the function to write the reversed poem to a new file
    write()
    # Call the function to append a name and message to the new file
    append()


if __name__ == "__main__":
    """
    Standard check to ensure main() runs only when the script is executed directly.
    """
    # Execute the main function
    main()