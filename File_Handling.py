f = open("trail.txt", "r")
print("\n1. Reading and printing whole file :\n", f.read())
f.close()

# read() function
f = open("trail.txt", "r")
print("\n2. Reading and printing first 10 character :\n", f.read(15))
f.close()

# readline() function
f = open("trail.txt", "r")
print("\n3. Reading and printing first line from file :\n", f.readline())  # after this f2 will point at last of line 1
print("4. Reading and printing second line from file :\n", f.readline())
print("5. Reading and printing third line till 5th character from file :\n", f.readline(5))
f.close()

# printing file using for loop
f = open("trail.txt", "r")
print("\n6. Printing element using for loop :\n")
for x in f:
    print(x)
f.close()

# Appending file
f = open("trail.txt", "a")  # if we use "w" instead of "a" then previous data will be overwritten with new data
f.write("\nThis is new appended line")
f.close()

f = open("trail.txt", "r")
print("\n7. File content after appending :\n", f.read())
f.close()

# "x" OR "w" can be used to create new file which doesn't exist in folder
f = open("New_File.txt", "w")
f.write("This is new file created.\nWe can create new file using \"x\" OR \"w\"")
f.close()
print("\n8. New file is created")
f = open("New_File.txt", "r")
print("9. Content in new file :\n", f.read())
f.close()

# To delete file
import os
os.remove("New_File.txt")  # Give filename as argument
print("\n10. New file deleted")

# Another way to delete file
if os.path.exists("New_File.txt"):
    os.remove("New_File.txt")
    print("New file deleted")
else:
    print("\n11. File doesn't Exists")
