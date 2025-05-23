# name = "Ankit"
# #       01234


# # String Slicing is used to access a range of characters in a string

# print(name[0:3])  # print the first three characters of name - Ank goes from 0 to 2
# print(name[0:-4])  # print the first four characters of name - An name[0: (5-4=1)]  will go from 0 to 1

name2 = "Ankit1234567890"

#print(name2[0:10:n]) # Skip n - 1 characters

print(name2[0:10:2])  # Skip 1 character each time: A, k, t, 1, 3 -> 'Akt13'
print(name2[0:10:3])  # Skip 2 characters each time: A, i, 1, 4 -> 'Ai14'

print(name2[:4]) # Replace the first empty number with 0
print(name2[4:]) # Replace the second empty number with length ie; 15
