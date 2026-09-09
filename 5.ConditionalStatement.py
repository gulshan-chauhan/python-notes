#Conditional Statement
#1.elif statement
num=float(input("Enter number for check positive or negative:"))
if(num>0):
    print("Positive")
elif(num==0):
    print("Zero")
else:
    print("Negative")
#neasted if condition
b=int(input("Enter age."))
marks=float(input("Enter marks:"))
if(b>=18):
    print("You are adult")
    if(marks>=33):
        print("pass")
        if(num%2==0):
            print("Num is even.")#It when both if condition are true
        else:
            print("Num is odd.")
    else:
        print("fail")
else:
    print("You are under 18.")


a=int(input("Entetr number for check division:"))
if(a%2==0 and a%5==0):
    print("A Devided by both")
elif(a%2!=0 and a%5==0):
    print("A devided by 5 only.")
elif(a%2==0 and a%2!=0):
    print("A devided by 2 only.")
else:
    print("A not devided by 5 or 2.")
