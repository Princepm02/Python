# Numbers
numbers = [1, 2, 3, 4, 90, 67]
print("Printing Numbers using for loop : ")
for x in numbers:
    print(x)

# String
st = "Prince"
print("Printing String using for loop : ")
for x in st:
    print(x)

# Numbers with break statement
numbers = [1, 2, 3, 4, 90, 67]
print("Printing Numbers using for loop and break statement : ")
for x in numbers:
    if x == 90:
        break  # at x=90 it will break fo loop
    print(x)

# Numbers with continue statement
numbers = [1, 2, 3, 4, 90, 67]
print("Printing Numbers using for loop and continue statement : ")
for x in numbers:
    if x == 90:
        continue  # it won't print value 90
    print(x)

# range
print("range(5) :")
for x in range(5):
    print(x)  # it won't print 5 as it is exclusive

print("range(5, 10) :")
for x in range(5, 10):
    print(x)  # it will print from 5 to 9 as 10 is exclusive

# while loop
print("\nWhile loop")
i=1
while i<6:
    print(i)
    i+=1
