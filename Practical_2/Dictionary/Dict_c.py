# 20CS010 - Meet Butani
# c. Write a Python program to sum all the items in a dictionary.
# ---------------------------------------------------------------

# creating a sample dictionary
dict = {'X':10, 'Y':15, 'Z':20}
sum = 0

# creating a 'for' loop that finds the sum of all values
for i in dict.values():
      sum+=i

# printing the dictionary
print(dict)

# printing the sum of all values of a dictionary
print("Sum of values is:", sum)