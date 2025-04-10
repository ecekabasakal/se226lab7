import math_utils

def main():
    operations = {
        "+": math_utils.add,
        "-": math_utils.subtract,
        "*": math_utils.multiply,
        "/": math_utils.divide,
        "": math_utils.power,
        "%": math_utils.mod
    }

    try:
        x = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /, **, %): ")
        y = float(input("Enter second number: "))

        if operator in operations:
            result = operations[operator](x, y)
            print(f"Result: {result}")
        else:
            print("Invalid operator!")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if _name_ == "_main_":
    main()
