def getMean(a,b,c,d,e,f,g,h,i):
    try:
        nums = [a,b,c,d,e,f,g,h,i]
        strt = 0
        for num in nums:
            num = int(num)
            strt+=num
        print(strt/len(nums))
    except ValueError:
        print("Enter integers only")           
    except ZeroDivisionError:
        print("Zero division not possible")    
        
getMean(1,2,3,4,5,6,7,8,9)

def getMode(a,b,c,d,e,f,g,h,i):
    try:
        nms = [a,b,c,d,e,f,g,h,i]
        for num in nms:
            num = int(num)
        mode = max(nms)
        print(mode)    
    except ValueError:
        print("Operation can not be perfomed on a non-integer")        

getMode(1,2,3,4,5,6,7,8,9)
