# Implement a checking system that should check a password only thrice.
# It should tell the user how many attempts are remaining
chances = 3 
while chances <4:
    try: 
        pwd = input("Write password")
        if pwd =="algosmith":
            print("Access granted")
            break
        else:
            chances -=1
            if chances > 0:
                print("Access denied \m You have ",chances," remaining")
            else:
                break            
    except:
        print("Error")           