# Q. Write a Python code to read an integer in a file e.g 123 and convert it to words
# e.g One hundred and twenty three and write the result back to the same file such that your
# file will have "123 One hundred and twenty three " in it
import inflect

def convert_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)

def main():
    file_name = "input_integer.txt"

    # Read integer from the file
    with open(file_name, "r") as file:
        integer = int(file.readline().strip())

    # Convert integer to words
    words = convert_to_words(integer)

    # Write result back to the file (overwrite original content)
    with open(file_name, "w") as file:
        file.write(str(integer) + " " + words)

if __name__ == "__main__":
    main()
