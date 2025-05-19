age = int(input("Enter your age: "))

if age > 18:
    print("You can drive.")
    print("Thank you!")
elif(age == 18):
    print("Lets schedule a driving test.")
    print("Thank you!")
elif(age == 0):
    print("You are not born yet.")
    print("Thank you!") 
else:
    print("You cannot drive.")
    print("Sorry!")
# The above code checks if the user is older than 18 and prints a message accordingly.
print("End of program.")