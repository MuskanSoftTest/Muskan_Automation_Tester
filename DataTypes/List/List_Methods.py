# Define a sample list
my_list = [3, 1, 4, 1, 5]

print("Original list:", my_list)

# Append
my_list.append(9)
print("append(9):", my_list, "- Adds 9 at the end")

# Extend
my_list.extend([2, 6])
print("extend([2, 6]):", my_list, "- Adds multiple items at the end")

# Insert
my_list.insert(2, 'a')
print("insert(2, 'a'):", my_list, "- Inserts 'a' at index 2")

# Remove
my_list.remove(1)
print("remove(1):", my_list, "- Removes first occurrence of 1")

# Pop
popped = my_list.pop()
print("pop():", my_list, "- Removes last element (was:", popped, ")")

# Index
index_val = my_list.index(4)
print("index(4):", index_val, "- Index of first occurrence of 4")

# Count
count_val = my_list.count(1)
print("count(1):", count_val, "- Counts how many times 1 appears")

# Sort
my_list2 = [5, 3, 8, 1]
my_list2.sort()
print("sort():", my_list2, "- Sorts the list")

# Reverse
my_list2.reverse()
print("reverse():", my_list2, "- Reverses the list")

# Copy
copy_list = my_list.copy()
print("copy():", copy_list, "- Makes a copy of the list")

# Clear
copy_list.clear()
print("clear():", copy_list, "- Empties the list")
