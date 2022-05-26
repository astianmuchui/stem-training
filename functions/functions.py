def getMean(a,b,c,d,e,f,g,h):
    sm = a+b+c+d+e+f+g+h
    return sm
    mean = sm/8
    return mean
    
def getMode(a,b,c,d,e,f,g,h):
    lis = [a,b,c,d,e,f,g,h]
    for x  in lis:
        x = int(x)
    mode = max(lis)
    return mode
def outputName(a):
    print("Hi",a)
def replacein(phrase):
    word = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            word = word+"g"
        else:
            word = word+letter
    return word
print(replacein(input("Enter phrase: ")))            
    