class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def details(self):
        print(f"my name is ",self.name," and my age is " ,self.age)
        
class Employee(person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
    def details(self):
        print(f"my name is ",self.name," and my age is " ,self.age," and my salary is ",self.salary)
        print("my salary is ",self.salary)
p2 = Employee("sarath",25,25000000)
p2.details()


