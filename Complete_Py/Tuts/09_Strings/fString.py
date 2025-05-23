# String formatting is used to format strings in a specific way

template = "Dear {}, You are selected! We can offer you a package of {} LPA. Your joining date is {}"

a = "Ankit" 
a1 = 10
a2 = "01-01-2024"

b = "Jethalal Gada"
b1 = 20
b2 = "01-01-2025"

# s1 = template.format(a, a1, a2)
# s2 = template.format(b, b1, b2)
# print(s1)
# print(s2)

# f-string is used to format strings in a specific way

print(f"Dear {a}, You are selected! We can offer you a package of {a1} LPA. Your joining date is {a2}")
print(f"Dear {b}, You are selected! We can offer you a package of {b1} LPA. Your joining date is {b2}")