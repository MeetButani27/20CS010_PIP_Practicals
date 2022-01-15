# 20CS010 - Meet Butani
# e. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# -------------------------------------------------------------

# creating 3 sample dictionaries
dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}

# printing all the 3 dictionaries
print(dict1)
print(dict2)
print(dict3)

# creating a new empty dictionary
dict = {}

# merging all the 3 dictionaries
dict.update(dict1)
dict.update(dict2)
dict.update(dict3)

# printing the dictionary
print(dict)