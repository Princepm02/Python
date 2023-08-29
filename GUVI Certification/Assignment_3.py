# Q.1. Write a code using a function to check whether a given number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))

result = check_even_odd(num)
print(f"The number {num} is {result}.")


# Q.2. Write a code using a function to check whether a given number is prime number or not
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Input number
n = int(input("Enter a number: "))

if is_prime(n):
    print(n, "is Prime Number")
else:
    print(n, "is NOT Prime Number")


# Q.3. Write a code to print a Fibonacci series upto the nth term.
#       Use the int(input()) to get an input from the user as well for the value of n.)
def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Input number of terms
n = int(input("Enter the value of n: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    series = fibonacci_series(n)
    print(f"Fibonacci Series up to {n} terms:", series)
