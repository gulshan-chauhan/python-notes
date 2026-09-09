#1.Airthmetic operator: +,-,*,/,%,**
x=10
y=5
print("Sum of x & y",x+y)
print("Reminder:",x%y ,"\nPower:",x**y)

#2.Comparison operator output true or false:==,!=,>,<,>=,<=
print("x is equal to y:",x==y,"\nx is less than y:",x<y)

#3.Logical operator:and ,or ,not
print(x>y and x<y)# both statement are true then print True
print(x>y or x<y)# any one statement are true then print True
print("Not operator result:",not(x>y))#It reverse value 

#4.Assignment operator
a=4.5#implicit type conversion
b=5
a+=6 #a=a+6
print(a)
b**=2
print(b)
b//=a#Devide // > It remove decimal value
print(b)
print(a+b)