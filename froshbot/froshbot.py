import cmath

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant: "))

disc = b**2 - 4*a*c

root1 = (-b - cmath.sqrt(disc)) / (2*a)
root2 = (-b + cmath.sqrt(disc)) / (2*a)

if disc == 0 or disc > 0:
    print(f"The roots are {root1} and {root2}")
elif disc < 0:
    Croot1 = cmath.sqrt(-disc) / (2*a)
    Croot2 = cmath.sqrt(-disc) / (2*a)
    Rroot1 = -b / (2*a)
    Rroot2 = -b / (2*a)
    print(f"The first root is {Rroot1} - i{Croot1}")
    print(f"The second root is {Rroot2} + i{Croot2}")