# Open a file for reading
with open('example.txt', 'r') as file:
    content = file.read()
    print("Read Entire File:\n", content)

# Create a new file if it doesn't exist
with open('example1.txt', 'w') as file:
    file.write("This is a new file created with 'w' mode.")

# Append content to a file
with open('example.txt', 'a') as file:
    file.write("\nThis line is appended using 'a' mode.")

# Read file in binary mode
with open('example.txt', 'rb') as file:
    binary_content = file.read()
    print("Binary Content:", binary_content)

# Read the entire file again
with open('example.txt', 'r') as file:
    content = file.read()
    print("Updated File Content:\n", content)

# Read first 10 characters
with open('example.txt', 'r') as file:
    content = file.read(10)
    print("First 10 Characters:", content)

# Read one line at a time
with open('example.txt', 'r') as file:
    line = file.readline()
    print("First Line:", line)

# Read all lines into a list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print("All Lines as List:", lines)

# Overwrite file content
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line overwritten.")

# Append more content
with open('example.txt', 'a') as file:
    file.write("\nThis line is appended again.")

# Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)

# Read entire file after changes
with open('example.txt', 'r') as file:
    content = file.read()
    print("Final Content:\n", content)

# Read specific parts using tell() and seek()
with open('example.txt', 'r') as file:
    print("Read 5 characters:", file.read(5))
    print("Current Position:", file.tell())
    
    file.seek(0)  # Move cursor to the beginning
    print("Read 5 characters again:", file.read(5))

# Check if file is closed
file = open('example.txt', 'r')
print("Is file closed?", file.closed)
file.close()
print("Is file closed?", file.closed)
