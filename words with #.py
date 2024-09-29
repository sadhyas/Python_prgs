# Open the text file for reading
file_name = input("Enter the name of the text file: ")

try:
    with open(file_name, 'r') as file:
        for line in file:
            # Split the line into words using whitespace as a separator
            words = line.strip().split()
            
            # Join the words with '#' as a separator and print
            result = '#'.join(words)
            print(result)

except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
