from math import sqrt

print("Please enter the length of the sides of the triangle.")
a = float(input("What is the length of one of the sides?"))
b = float(input("Enter the length of the other side"))
c = sqrt(a**2 + b**2)
print(f"The hypotenuse of a right triangle with sides measuring {a} and {b} is {c}.")