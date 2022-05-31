#  class for person , student and teacher 
#  person class is parent class 
#  @params name , dob ,height ,weight
# method to compute theage , BMI

# student should inherit peson class, add the class in which the student is studying, favourite subject

# teacher should inherit person class , add the class in which the teacher teaches , salary 
class person:
    def __init__(self, name, dob, height, weight):
        self.name = name
        self.dob = dob
        self.height = height
        self.weight = weight
    def date_of_birth(self):
            dob = self.dob
            print(dob)
    def age(self):
            self.year = 2022
            age = self.year - self.dob
            print(age)
    def height(self):
            height = self.height
            print(height)
    def weight(self):
            weight = self.weight
            print(weight)
    def bmi(self):
        bmi = self.weight / (self.height **2)
        print(bmi)
class student(person):
    def __init__(self, name, dob, height, weight, class_studying, favourite_subject):
        super().__init__(name, dob, height, weight)
        self.class_studying = class_studying
        self.favourite_subject = favourite_subject
    def class_studying(self):
        class_studying = self.class_studying
        print(class_studying)
    def favourite_subject(self):
        favourite_subject = self.favourite_subject
        print(favourite_subject)
        
class teacher(person):
    def __init__(self, name, dob, height, weight, class_teaching,subject_teaching, salary):
        super().__init__(name, dob, height, weight)
        self.class_teaching = class_teaching
        self.subject_teaching = subject_teaching
        self.salary = salary
    def class_teaching(self):
        class_teaching = self.class_teaching
        print(class_teaching)
    def salary(self):
        salary = self.salary
        print(salary)    
    def teaching_subject(self):
        subject_teaching = self.subject_teaching
        print(subject_teaching)    
# instantiate 
x = person(name="John",dob= 2000, height=5, weight=150)
y = student(name="Jane", dob=2000, height=5, weight=150, class_studying="1st", favourite_subject="Maths")
z = teacher(name="Jack", dob=2000, height=5, weight=150, class_teaching="1st", subject_teaching="Maths",salary=55000)
z.teaching_subject()