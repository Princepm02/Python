# List
lt = ['car', 'bus', 'truck']


def loop(x):
    print(x * 3)


print("1. Printing Items of the list 3 times")
loop(lt)

# List Properties: Ordered (Maintains insertion order/index), Changeable, Allows duplicates
lt = ['car', 'bike', 90, 30, True, 45.56, False, 3.00]

print("\n2. Elements in the list:", lt)
print("3. Length of List:", len(lt))
print("4. Type of List:", type(lt))

# Slicing
print("\n5. Elements in the list[2:5]:", lt[2:5])  # Prints elements from index 2 to 4
print("6. Elements in the list[2:]:", lt[2:])  # Prints elements from index 2 to the end
print("7. Elements in the list[:5]:", lt[:5])  # Prints elements from start to index 4

# Replacing items in the list
lt[3] = "new element"
print("\n8. Elements after replacing in the list:", lt)

lt[1:3] = ["Watermelons", "hero honda"]
print("\n9. Elements after replacing in the list:", lt)

# Inserting an element in the list
lt.insert(3, "java69")
print("\n10. Elements after inserting an element in the list:", lt)

# Appending (inserting at the end of the list) an element to the list
lt.append("last element")
print("\n11. Elements after appending an element in the list:", lt)
