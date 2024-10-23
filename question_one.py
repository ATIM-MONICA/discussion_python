# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 

#1st approach using input function
temperature = float(input("Enter the temperature value in degree 'C': "))
if temperature < 0:
     print("Freezing")
elif temperature >= 0 and temperature <= 10:
     print("Cold")
elif temperature >=11 and temperature <=20:
       print("Moderate")
elif temperature >=21 and temperature <=30:
     print("Warm")
else:
       print(f"It is Hot")
       

# 2nd approach using def function:
def classify_temperature(temp):
    if temp < 0:
        return "Freezing"
    elif 0 <= temp <= 10:
        return "Cold"
    elif 11 <= temp <= 20:
        return "Moderate"
    elif 21 <= temp <= 30:
        return "Warm"
    else:
        return "Hot"

temperature = float(input("Enter the temperature: "))
classification = classify_temperature(temperature)

print(f"The temperature is classified as: {classification}")




# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**3. What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and provide the answer in 1 decimal place
 
#approach 1 
radius = float(input("Enter the radius: "))
import math
pie = math.pi
volume_of_the_sphere = (4/3)*pie*radius**3
print(f"The volume of the sphere with radius {radius} is {volume_of_the_sphere:.1f}")


#approach 2
def volume_of_the_sphere():
   radius = float(input('Enter the radius of the sphere:'))
   import math
   pie = math.pi
   volume = (4/3)*pie*radius**3
   print(f'The volume of the sphere whose radius is {radius} is {volume:.1f}')
volume_of_the_sphere()

# OR

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return round(volume, 1)
radius = float(input("Enter the radius of the sphere: "))
volume = sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} is {volume}")


    
