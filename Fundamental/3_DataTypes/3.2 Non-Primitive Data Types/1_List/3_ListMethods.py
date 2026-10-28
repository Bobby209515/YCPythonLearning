# Methods is a used to perform to task but dependent on the class or object.

print("List Methods")

list1 = [1, 2, 3, 4, 5, 3, 5, 3]
print("Original List:", list1)

list1.append(6)
print("List after append:", list1)

list2 = [7, 8, 9]
list1.extend(list2)
print("List after extend:", list1)

count = list1.count(3)
print("Count of 3 in the list:", count)

name_list = ["Alice", "Bob", "Charlie", "David", "Alice"]
count = name_list.count("Alice")
print("Count of the name Alice in the name list:", count)