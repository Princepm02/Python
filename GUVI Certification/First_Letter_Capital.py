# Q.1. Get a list of name as an input from the user and make the first letters in caps and print each word as a list
# Get a list of names from the user
input_names = input("Enter a list of names separated by spaces: ").split()

# Capitalize the first letter of each name and store them in a new list
capitalized_names = [name.capitalize() for name in input_names]

# Print the capitalized names as a list
print("Capitalized names:", capitalized_names)
