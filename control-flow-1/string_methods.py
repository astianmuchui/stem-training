ops = ['*',"+","-","/","%"]
string = "19*50"
for op in ops:
    if op in string:
        y = string.index(op)
        fnum = float(string[:y])
        snum = float(string[y+1:])
        if op =="+":
            a = fnum+snum
            print(a)
        elif op =="-":
            s = fnum-snum
            print(s)
        elif op =="/":
            d = fnum/snum
            print(d)
        elif op =="*":
            mt= fnum*snum   
            print(mt)
        elif op == "%":
            m = fnum%snum
            print(m)             