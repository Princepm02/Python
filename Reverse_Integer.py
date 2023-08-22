# Q. Write a Python code to reverse the given integer and print the integer
def reverse_integer(n):
    reversed_n = 0
    while n > 0:
        last_digit = n % 10
        reversed_n = reversed_n * 10 + last_digit
        n //= 10
    return reversed_n

# Get an integer from the user
num = int(input("Enter an integer: "))

# Reverse the integer
reversed_num = reverse_integer(num)

# Print the reversed integer
print("Reversed integer:", reversed_num)
