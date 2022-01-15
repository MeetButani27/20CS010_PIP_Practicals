# 20CS010 - Meet Butani
# b. Write a Python script to merge two Python dictionaries.
# ---------------------------------------------------------

# creating 2 sample dictionaries
dict1 = {'A':1, 'B':2, 'C':3}
dict2 = {'X':8, 'Y':9, 'Z':10}

# printing both the dictionaries
print(dict1)
print(dict2)

# merging dict2 after dict1 dictionary
dict1.update(dict2)

# printing the merged dict1
print(dict1)