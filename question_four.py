#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.

# Initial list of five favorite foods
favorite_foods = ["Pizza", "Sushi", "Burgers", "Pasta", "Ice Cream"]

# Add two more items to the list
favorite_foods.append("Tacos")
favorite_foods.append("Salad")

# Remove one item from the list
favorite_foods.remove("Ice Cream")

# Print the updated list
print(f"Updated favorite foods list: {favorite_foods}")



#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.

numbers = [2, 5, 8, 10, 3, 6]

# Print the first and last elements of the list
first_element = numbers[0]
last_element = numbers[-1]
print(f"First element: {first_element}")
print(f"Last element: {last_element}")
#print the last in reversed order
reversed_list = numbers[::-1]
print(f"Reversed list: {reversed_list}")
#print the sum of all the elements in the list
sum_of_elements = sum(numbers)
print(f"Sum of all elements: {sum_of_elements}")

