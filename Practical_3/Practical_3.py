# 20CS010 - Meet Butani
# Find the Captain's Room Number from the given list of Room numbers
# ------------------------------------------------------------------

# taking input from the user
k = int(input())

# reading the list elements from the user
lst = list(map(int, input().split()))

# finding and printing the captain's room number
if len(lst)%k == 1:
    for i in lst:
        if lst.count(i) == 1:
            print("Captain's room number is:", i)
            break

else:
    print("Invalid input !!")
