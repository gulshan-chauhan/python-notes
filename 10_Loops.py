# While loop & For loop
num=1
while num<=5:
    print("Goldie")
    num=num+1
print("Now we are out of the while loop")
#Write a program to print number from 10 down to 1 using a while loop
j=5
while j>=1:
    print(j)
    j=j-1
print("Done")
# Print all even no.2,4,6
n=1
while n<=10:
    if(n%2==0):
        print(n)
    n=n+1
# Print the sum of first n natural no. Output should be 3+2+1=6
e=int(input("Enter a no to get sum of natural no:"))
sums=0
while e>=1:
    sums=sums+e
    e=e-1
print("Sum=",sums)
print("Last value of e=",e)#also 0