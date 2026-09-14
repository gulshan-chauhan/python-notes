# It store multiple values & different data types in a single variable
food=["Apple","Mango",7.7]
print(food)
print(food[-1:],food[0])#Indexing
#List are mutable
marks=[10,33,33,3]
print(marks)
marks[1]=88 # Update value at index 1
print(marks)
#Slicing    
print(marks[1:3])
#List function
print("Length of food list:",len(food))#Return length of list
print("Largest value in marks list:",max(marks))#Return largest value of list
print("Smallest value in marks list:",min(marks))#Return smallest value of list

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
print(marks.count(33))#Count the number of times a value occurs in list
print(marks.index(33))#Return the index of first occurrence of value
marks.reverse()#Reverse the list
print(marks)
lis2=[44,44,56]
marks.extend([lis2])#Add multiple values at the end of list
print(marks)
marks.clear()#Remove all elements from list
print(marks)