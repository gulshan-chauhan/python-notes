import time
#range (start"0",stop,add/step/gap"1 default value")
for item in range(2,21,2):#multiple of 2 or even no.
    print(item)
for i in range(1,21,2):#odd no.
    print("odd no:",i)
for n in range(1,6):
    pass #empty nothing to do here 

#Print a countdown timer with gap of 1 second
count=int(input("Enter the counter n:"))
print("\n Countdown start Now:")
for count in range(count,0,-1):
    print(count)
    time.sleep(1)#in second
print("\n Happy New Year ")