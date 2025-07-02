def add(a,b):  # positional arguments
    x = a + b
    return x

c = add(10, 20)
print(c)  # Output: 30


def add_with_default(a, b, p=5):  # default argument
    x = a + b + p
    return x

d = add_with_default(10, 20)
print(d)  # Output: 35


z = add(b=10, a=20)  # keyword arguments
print(z)  # Output: 30