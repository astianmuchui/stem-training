words = ["I","did","A"]
for word in words:
    print(word + "!")
    
 #search a string
count = 0 
str = "Hello guys welcome back to my class"
# for x in str:
#     if x == "o":
#         count+=1
# print("There are " ,count," O's")

# Program that removes characters 

# for x in str:
#     if x != 'l':
#         print(x)
        
outstr = ""        
for x in str:
    if x == "l" or x =="e" or x =="u":
        continue
    else:
        outstr +=x                
print(outstr)               