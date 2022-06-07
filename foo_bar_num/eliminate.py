def elimin(n):
    n = int(n)
    for i in range(n):
        if i > 10:
            print("Greater than 10")
        else:
            print(i)
elimin(17)

def greater(a,b):
    a = int(a)
    b = int(b)
    for i in range(b):
        if i > a:
            print(f"Greater than {a}")
        else:
            print(f"Less than {a}")
greater(8,30)


