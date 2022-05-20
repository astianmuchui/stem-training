print("Welcome : Complex calculator")
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
#  Re-Declare and convert to integers
first_number = int(first_number)
second_number = int(second_number)
print("Select an operator , Options : [+ , * , / , % , - ]")
operator = input("Enter operator: ")
ans = "answer = "
if '*' == operator:
    print(ans,first_number*second_number)
elif '+' == operator:
    print(ans,first_number+second_number)
elif '-' == operator:
    print(ans,first_number-second_number)
elif '/' == operator:
    print(ans,first_number/second_number)
elif '%' == operator:
    print(ans,first_number%second_number)
else:
    print("Operator does not exist")