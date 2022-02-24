# 20CS010 - Meet Butani
# Lapindrome is defined as a string which when split in the middle, gives 2 halves having the same characters and same frequency
# of each character. If there are odd no. of characters in the string, we ignore the middle character and check for lapindrome.
# For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency.
# Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome as the 2 halves contain
# the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome.
# ------------------------------------------------------------------------------------------------------------------------------------

# reading the total no. of words 'n' from the user
n = int(input())

# reading 'n' different words from the user and checking for Lapindrome
for _ in range(n):
    str = input()

    # finding the length of the given string
    n = len(str)

    # slicing the first half of the given string
    s1 = str[0:int(n/2)]

    # slicing the second half based on length of the given string
    if n%2==0:
        s2 = str[int(n/2): ]
    else:
        s2 = str[int(n/2)+1: ]

    # checking whether both parts are equal or not and printing required answer
    if sorted(s1)==sorted(s2):
        print("YES")
    else:
        print("NO")
