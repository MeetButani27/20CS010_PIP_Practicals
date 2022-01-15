# 20CS010 - Meet Butani
# e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
# ---------------------------------------------------------------------------------------------------------

# function to find the most common element and their counts
def mostCommon(list):
    answer,count, value = 0, 0, 0
    list.sort()

    for i in range(len(list)-1):
        if list[i]==list[i+1]:
            count+=1
            if(count >= answer):
                answer = count
                value = list[i]
        else:
            count=0

    return value, answer+1


### For List:
list = [1, 4, 7, 4, 8, 9, 4, 7, 2, 5]
print(list)
# calling the mostCommon() function
print("Most common element & it's frequency is:", mostCommon(list))
print()


### For Tuple:
tuple = (1, 3, 8, 3, 2, 3, 4, 1, 3, 3)
print(tuple)
list = []
# converting tuple into list
for i in tuple:
    list.append(i)

# calling the mostCommon() function
print("Most common element & it's frequency is:", mostCommon(list))
print()


### For Dictionary:
dict = {'Y1': 2021, 'Y2': 2018, 'Y3': 2021, 'Y4': 2017, 'Y5': 2021}
print(dict)
list = []
# converting dictionary into list
for i in dict:
    list.append(dict[i])

# calling the mostCommon() function
print("Most common element & it's frequency is:", mostCommon(list))