#Question 3
# Using loop of your choice, WITI  has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89% Grade is   B
# 70% - 79% Grade is   C                                                        
# 60% - 69%  Grade is  D                  
# 50% - 59%  Grade is  E  
# < 50%                Fail 

# Function to determine grade based on the score
def calculate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif 50 <= score <= 59:
        return "E"
    else:
        return "Fail"

# Loop to take input for multiple students and display their grades
def grade_students():
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        score = int(input(f"Enter the score for student {i+1}: "))
        grade = calculate_grade(score)
        print(f"Student {i+1}'s grade: {grade}")
        
grade_students()