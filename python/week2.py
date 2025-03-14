# 1. Create an empty list called my_list.
# 2. Append the following elements to my_list: 10, 20, 30, 40.
# 3. Insert the value 15 at the second position in the list.
# 4. Extend my_list with another list: [50, 60, 70].
# 5. Remove the last element from my_list.
# 6. Sort my_list in ascending order.
# 7. Find and print the index of the value 30 in my_list.

# Step 1
my_list = []

# Step 2
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3
my_list.insert(1, 15)

# Step 4
my_list.extend([50, 60, 70])

# Step 5
my_list.pop()

# Step 6
my_list.sort()

# Step 7
index = my_list.index(30)
print(index)

print(my_list)