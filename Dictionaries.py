# Dictionaries
# Dictionaries Properties: Unordered (Doesn't Maintains insertion order/index), Changeable, DO NOT Allows duplicates
dictt = {
    "name": "Prince",
    "age": 21,
    "height": 6.1,
    "age": 20  # here value will be overwritten but key duplication is not allowed
}
print("\n19. Element in Dictionary : ", dictt)
print("20. Length of dictionary : ", len(dictt))

# We can also use list inside dictionary
dictt = {
    "name": "Prince",
    "age": 21,
    "vehicle": "Bullet",
    "height": 6.1,
    "fruits": ["apple", "mango", "banana"]
}
print("\n21. Element in Dictionary(with list) : ", dictt)
print("22. Type of dictionary with list : ", type(dictt))

# Fetching data from dictionary
x = dictt["age"]
print("\n23. Age - dictt[\"age\"] : ", x)
x = dictt.get("age")
print("\n24. Age - dictt.get(\"age\") : ", x)

x = dictt["fruits"]
print("\n25. fruits - dictt[\"fruits\"] : ", x)
x = dictt.get("fruits")
print("\n26. fruits - dictt.get(\"fruits\") : ", x)

# Replacing/Updating value in dictionary
dictt["vehicle"] = "Lord Splendor"
print("\n27. Element in Dictionary after replacing/updating value for vehicle : ", dictt)

# Updating value using update method
dictt.update({"name": "Prince Mishra"})
print("\n28. Element in Dictionary after updating name using update function : ", dictt)

# Adding new key and value in dictionary
dictt["colour"] = "RED"
print("\n29. Adding value to last in dictionary : ", dictt)

# Deleting element from dictionary using pop function
dictt.pop("colour")
print("\n30. After deleting colour from dictionary using pop function : ", dictt)
