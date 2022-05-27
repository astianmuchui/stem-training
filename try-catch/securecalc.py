print('Welcome: Complex calculator')
while True:
    try: 
        int_one = int(input("Enter first number: "))
        int_two = int(input("Enter second number: "))
        op = input("Enter operator, Options:  {+,-,*,/,%}")
        if op =="+":
            print(int_one+int_two)
        elif op =="-":
            print(int_one-int_two)
        elif op == "*":
             print(int_one*int_two)
        elif op == "/" :
            print(int_one/int_two)
        elif op == "%" :
            print(int_one%int_two) 
        else:
             print("operator does not exist")
                
    except  ValueError:
        print("Value error")
    except ZeroDivisionError:
        print("Division by zero is'nt possible")
        