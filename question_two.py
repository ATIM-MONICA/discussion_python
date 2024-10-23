# Question 2(i)

# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)  
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi, 2), category

weight = float(input("Enter the weight: "))
height = float(input("Enter the height: "))
bmi, category = calculate_bmi(weight, height)

print(f"BMI: {bmi}, Category: {category}")




# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)

import math
# Function to calculate the volume of a cylinder
def calculate_cylinder_volume(radius, height):
    volume = math.pi * (radius ** 2) * height 
    return round(volume, 2)

radius = 5 
height = 10 
volume = calculate_cylinder_volume(radius, height)
print(f"The volume of the cylinder is {volume} ")


