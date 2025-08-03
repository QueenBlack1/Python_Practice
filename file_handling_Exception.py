def modify_content(content):
    """
    Example modification: convert all text to uppercase.
    You can change this function to do any modification you want.
    """
    return content.upper()

def main():
    filename = input("Enter the filename to read: ")

    try:
        # Open the original file and read its content
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Cannot read the file '{filename}'. Please check the file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
