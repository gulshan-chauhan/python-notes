# print * in increcing and descreaging form
for i in range(1,6):
    print("*"*i)
for i in range(5,0,-1):#Decrease by one
    print("*"*i)

# Print even no.
i=0
while i<=10:
    i=i+2
    print("Even no.",i)
# Print odd no.
o=-1
while o<=10:
    o=o+2
    print("Odd no.",o)
# Print a Table of any no.
n=int(input("Enter a no. for Multiplication:"))
i=1
while i<=10:
    print(f"{n}x{i}={n*i}")
    i=i+1
#Print this pattern using while loop
#*
#** upto 4 ****
s=1
while s<=4:
    print("*"*s)
    s=s+1
#*** changed pattern
#**
#*
g=4
while g>=1:
    print("*"*g)
    g=g-1