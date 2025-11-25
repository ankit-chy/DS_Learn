#Q1: Your First Program
#Write a program that prints:
print("Hello, World! Welcome to Python.")


# Q2: Print a Poem
# Write a program that prints the following poem using a single print() statement:

# (Hint: Use \n for a new line.)

# Twinkle, twinkle, little star,
# How I wonder what you are!

print("Twinkle, twinkle, little star,\nHow I wonder what you are!")

# Q3: Variables & Data Types
# Create variables to store:

# Your name (string)
# Your age (integer)
# Your height in meters (float)
# A boolean value representing whether you are a student
# Print all of them in one line.

name = "Ankit"
age = 25
height = 1.65
is_student = True
print(name, age, height, is_student)


# Q4: Typecasting Practice
# You are given a string:

# num = "45"

# Convert it into an integer
# Add 10 to it
# Print the result

num = "45"
num_int = int(num)
result = num_int + 10
print(result)

# Q5: Taking User Input
# Write a program that:

# Asks the user for their favorite food.
# Prints:
# Wow! I also like <food>.

print("Tell your favourite fruit!")
fav_fruit = str(input())

print(f"Wow! I also like {fav_fruit}.")