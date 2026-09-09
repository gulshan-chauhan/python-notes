# It store multiple values & different data types in a single variable
food=["Apple","Mango",7.7]
print(food)
print(food[-1:],food[0])#Indexing
#List are mutable
marks=[10,33,33,3]
print(marks)
marks[1]=88
print(marks)
#Slicing
print(marks[1:3])
#List function
print(len(food))#Return length of list
print(max(marks))#Return largest value of list
print(min(marks))#Return smallest value of list

#Methods in list
marks.append(90)#Adds element at the end
print(marks)
marks.sort()#Ascending order
print(marks)
marks.pop(1)#Remove any index value
print(marks)
marks.remove(3)#Remove value
print(marks)
marks.insert(1,100)# Add value in any index
print(marks)