# 20CS010 - Meet Butani
# c. Write a Python program to add an item in a tuple.
# ----------------------------------------------------

# creating a sample tuple
tuple1 = (1, 2, 3, 4, 5, 6, 7)

# printing the tuple
print(tuple1)

# converting the tuple into list
list1 = list(tuple1)

# adding an element 8 to the list
list1.append(8)

# converting the list back into tuple
tuple1 = tuple(list1)

# printing the updated tuple
print(tuple1)