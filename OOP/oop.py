# OBJECT ORIENTED PROGRAMMING
class dog:
    def __init__(self,no_of_eyes,color,legs):
        self.no_of_eyes= no_of_eyes
        self.color = color
        self.legs = legs
    def barking(self):
        print("woof woof")
    def biting(self):
        print("The dog bites")    
        pass
german_shepherd = dog(no_of_eyes = 2,color = "grey",legs=2)
dodger = dog(no_of_eyes=1,color='green',legs=4)
dobberman = dog(2,'brown',4)

print(german_shepherd.color,german_shepherd.no_of_eyes  )
print(dodger.no_of_eyes)
dobberman.color = "gray50"
print(dobberman.color)  
print(dobberman.legs)
dobberman.barking()
dobberman.biting()
