# Append
fruits = ["apples","oranges","banana"]
fruits.append("cherry")
print(fruits)
#  Remove 
fruits.remove("cherry")
print(fruits)

#  pop

myfruits = fruits.pop(0)
print(myfruits)

# Clear

fruits = fruits.clear()

print(fruits)

vegs = ["apple","cherry","tomato"]
fr = ["pineapple","avocado"]
total = vegs+fr
print(total)

vegs.extend(fr)
print(vegs)
#  TUPLES
fr_tuple = ("apple","cherry","oranges")
print(fr_tuple)
print(fr_tuple[1])
#  inter-conversions
new_list = list(fr_tuple)
new_list.append("tomato")

fr_tuple = tuple(new_list)
print(fr_tuple)

#  Sets 
fruits_five = {"apples","oranges","oranges","oranges"}
print(fruits_five)

o_lis = [] 
mylist = [2,4,1,7,8,10,12]
print(mylist)
for i in mylist:
    o_lis.append(i)
    
# print(o_lis)    

#  short hand
for elem in mylist:
        if elem%2 == 0:
            o_lis.append(elem) 
print(o_lis) 
m_list = [x for x in mylist if x %2 ==0]
print(m_list)

def addnums(a,b):
    return a+b
res = addnums(14,6)
print(res)