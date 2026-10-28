list1 = [1,4,5,6,7,8]  # or list1 = list(1,4,5,6,7,8)  # Constructor for list1
list2 = [2,4,5,8,10,12] # or list2 = list(2,4,5,8,10,12)  # Constructor for list2

# 1. Convert the lists to sets
set1 = set(list1)
set2 = set(list2)

print("set1:", set1)
print("set2:", set2)

#2. Find the common values between the two sets
set3 = set1 & set2
print("set3:", set3)