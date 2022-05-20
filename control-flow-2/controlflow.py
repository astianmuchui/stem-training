"""
Day two of control flow Advance in if  statements , intro to loops 
Lists , Indexes , lists ,  Nested lists
"""

x= 4
if x<=1:
    print("Hey, Im still here")
    x -=1
    
print("Done")   

# Else statements
y = 2
if y == 10:
    print(y)
else:
    print("Not 10")    
    
    
# Simple grading system 
grade = int(input("Write score : "))

if grade>=80 and grade<=100:
    print("Student got A")
elif grade >= 70 and grade<80:
    print("Student got a B")
elif grade>=60 and grade <70:
    print("Student got C")
elif grade>=50 and grade <60:
    print("Student got D")
elif grade>0 and grade <50:
    print("Student got E")        