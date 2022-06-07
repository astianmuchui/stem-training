def sieve(num):
    num = int(num)
    for i in range(num):

        if i % 3 == 0 and i % 5 ==0:
            print(f"Foobar - {i}")
        elif i % 3 == 0:
                print(f"Foo - {i}")
        elif i % 5 == 0:
            print(f"Bar - {i}")
        else:
            print(i)
sieve(15)
    
    