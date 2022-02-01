# 20CS010 - Meet Butani
# Find the runner's-up score from the given list of scores.
# --------------------------------------------------------

# Reading total no. of elements from user
num = int(input())

# Reading the list of all elements entered by the user
lst = list(map(int, input().split()))

# Converting the inputted list into a set
st = set(lst)

# Sorting the elements of the set
if num == len(lst):
    st = sorted(st)

# Printing the second largest element
print("Runner's-Up score is:", st[len(st)-2])