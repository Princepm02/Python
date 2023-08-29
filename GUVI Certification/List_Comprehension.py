# List Comprehension
fruits = ["apple", "mango", "banana", "kiwi", "chiku"]
print("\nList Comprehension\n31. Element in fruit list : ", fruits)
a_fruits = []
for x in fruits:
    if "a" in x:  # It will copy only those element which contains letter "a"in it.
        a_fruits.append(x)
print("32. Element in a_fruits list which contain letter a : ", a_fruits)  # kiwi and chiku will NOT be copied

# List Comprehension in one line
i_fruits = [x for x in fruits if "i" in x]
print("33. Element in i_fruits list which contain letter i : ", i_fruits)  # kiwi and chiku will be copied

# to copy all element from one list to another
new_fruits = [x for x in fruits]
print("34. All copied elements in new_fruits : ", new_fruits)

# array
arr = [x for x in range(10)]
print("\n35. List comprehension with range function : ", arr)

# Converting to upper case and then copying all element from one list to another
new_fruits = [x.upper() for x in fruits]
print("\n36. All copied elements in UPPER case in new_fruits : ", new_fruits)
