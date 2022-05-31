# instantiate class from schools.py
from school import School
from inventory import library as lb
x = School(725,"Mumbai")
y = School(828,"Nairobi")
z = School(150,"Kampala")
# call say_motto() method
x.say_motto()
print(x.no_of_students)
lb.books()