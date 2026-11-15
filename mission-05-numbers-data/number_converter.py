# Number converter: decimal to binary and hexadecimal

text = input("Enter a positive decimal number: ")
number = int(text)

binary = bin(number)[2:]
hexadecimal = hex(number)[2:]

print("Binary:", binary)
print("Hexadecimal:", hexadecimal)