try:
    div = 10/0
    value = int(input("Enter first number: "))
    print(value)
except ValueError:
    print("Invalid number entered")
except ZeroDivisionError:
    print("Division by zero")