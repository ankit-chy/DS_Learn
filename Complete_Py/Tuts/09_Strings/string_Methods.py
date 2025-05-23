name = "Ankit"

# String are immutable
# name[0] = "X"  # This will give an error because strings are immutable - runtime error

# String Methods

# a = len(name)  # length of string
# print(a)  # print the length of name - 5

# String Methods
s ="hEllO WorLD"

print(s.upper() , s)  # convert string to uppercase
print(s.lower())  # convert string to lowercase
print(s.title())  # convert string to title case
print(s.capitalize())  # convert first char to upper case of string
print(s.swapcase())  # convert string to swap case


text = " \nHello World HeLLOO WOrlDss "
print(text)
print(text.strip())  # remove leading and trailing spaces
print(text.lstrip())  # remove leading spaces (left side)
print(text.rstrip())  # remove trailing spaces (right side)

text2 = "Learning Python is fun and is also easy"
print(text2.find("is"))  # find the index of first occurrence of "is" in string

print(text2.replace("is", "was"))  # replace all occurrences of "is" with "was"

text3 = "Apple, Banana, Orange, Mango"
print(text3)
print(text3.split(","))  # split the string into a list of strings using "," as separator

print(",".join(['Apple', ' Banana', ' Orange', ' Mango']))

text4 = "Python123"

print(text4.isalnum())  # check if string is alphanumeric
print(text4.isalpha())  # check if string is alphabetic
print(text4.isdigit())  # check if string is numeric
print(text4.islower())  # check if string is lowercase
print(text4.isupper())  # check if string is uppercase
print(text4.isnumeric())  # check if string is numeric
print(text4.isspace()) #