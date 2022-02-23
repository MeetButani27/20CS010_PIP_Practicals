# 20CS010 - Meet Butani
# You are given n words. Some words may repeat. For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word.
# ----------------------------------------------------------------------------------

# reading total no. of words 'n' from the user
n = int(input())

# creating an empty dictionary
dict = {}

# reading 'n' words from the user and inserting them into dict
for _ in range(n):
    word = input()

    # if word is already present in dict then incrementing its count
    # else adding the new word to the dict
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1

# printing the length of dict
print(len(dict))

# printing the required output
for i in dict:
    print(dict[i], end=" ")