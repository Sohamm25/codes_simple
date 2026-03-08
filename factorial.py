user_input = input("Enter elements of the list separated by spaces: ")
user_list = user_input.split()

user_list = [int(x) for x in user_list]
print(user_list)
print(min(user_list))

print(max(user_list))

