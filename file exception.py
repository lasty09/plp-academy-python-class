def process_file():

    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
        modified_content = content.upper()

    
        word_count = len(content.split())

        
        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)
            outfile.write(f"\n\nWORD COUNT: {word_count}\n")

        print("Success! 'output.txt' has been created with processed content.")

    except FileNotFoundError:
        print(" Error: The file does not exist.")
    except IOError:
        print(" Error: The file could not be read.")

process_file()