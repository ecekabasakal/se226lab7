def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y

if _name_ == "_main_":
    print("Testing math_utils.py")
    print(f"Add: {add(2, 3)}")
    print(f"Subtract: {subtract(5, 2)}")
    print(f"Multiply: {multiply(4, 3)}")
    print(f"Divide: {divide(10, 2)}")
    print(f"Power: {power(2, 3)}")
    print(f"Mod: {mod(10, 3)}")
