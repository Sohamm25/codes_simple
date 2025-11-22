user_input = input("Enter elements of the list separated by spaces: ")

# Split the input string into individual elements
user_list = user_input.split()

# Convert elements to appropriate data type if needed
# For example, if you want integers: 
user_list = [int(x) for x in user_list]
print(user_list)
print(min(user_list))

print(max(user_list))
