a =  int(input("Enter a lucky number: "))

match a :
    case 1:
        print("You are lucky!")
    case 34:
        print("You are lucky")
    case _:
        print("You are not lucky!")
# The underscore (_) is a wildcard that matches any value not explicitly handled by the previous cases.