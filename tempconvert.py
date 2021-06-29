def convert(s):
    f = float(s)
    c = (f -32) * 5/9
    return c

print("Enter temp in fahrenheit: ")
a = float(input())
print("The temp in celsius is", convert(a))