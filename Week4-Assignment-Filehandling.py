# Week 4 Assignment: File Read & Write with Error Handling

def modify_content(content: str) -> str:
    """
    Modify the file content.
    For this example: make everything uppercase.
    You can tweak this as you like (e.g., replace words, add line numbers).
    """
    return content.upper()


def process_file(input_filename: str, output_filename: str):
    try:
        # Read the input file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify the content
        modified_content = modify_content(content)

        # Write to the new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ File processed successfully! Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You don’t have permission to read/write this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Ask user for input file
    input_file = input("Enter the filename to read: ")
    output_file = "modified_" + input_file  # e.g., input.txt → modified_input.txt

    process_file(input_file, output_file)
