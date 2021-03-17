import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid Input")
    sys.exit(1)

try:
    print("Division of {x} and {y} :", x/y)
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

#https://docs.djangoproject.com/en/3.0/howto/windows/

#http://127.0.0.1:8000/
