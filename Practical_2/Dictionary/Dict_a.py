# 20CS010 - Meet Butani
# a. Write a Python script to check whether a given key already exists in a dictionary.
# -------------------------------------------------------------------------------------

# creating a sample dictionary
dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}

# function which checks whether the key is present in the dictionary or not
def isKeyPresent(key):
      if key in dict.keys():
            print("Key is present!")
      else:
            print("Key is not present!")

# printing the dictionary
print(dict)

# calling the function with different arguements(keys)
isKeyPresent('A')
isKeyPresent('M')
