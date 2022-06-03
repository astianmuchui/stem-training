while True:
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        z = x/y 
        print(z)
    except ZeroDivisionError:
        print("Zero division error")
    except ValueError:
        print("You did not enter a number")
    # else:
    #     print("Unknown error")
    finally:
        print("Program completed")