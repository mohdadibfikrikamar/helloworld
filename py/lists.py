# ## Lists
# 1. Create a grocery list and perform various  operations.
# 2.Write a program that finds the largest and smallest number in list

# 1

# grocery_list = ["milk", "eggs", "bread", "butter", "cheese"]

# print(len(grocery_list))
# print("milk" in grocery_list)
# print("tomato" in grocery_list)
# print(grocery_list[4])
# grocery_list.append("tomato")
# print(grocery_list)

# new grocery_list data = ["milk", "eggs", "bread", "butter", "cheese", "tomato"]

# num = [5, 10, 15, 20, 25, 30]

# print("Largest number in the list:", max(num))
# print("Smallest number in the list:", min(num))

##
count = 0
number = int(input("Enter a number: "))

while count <= number:
    count += 1


print("Smallest number in the list:", min(range(count)))
print("Largest number in the list:", max(range(count)))
