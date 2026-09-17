#For loop
food=["cake","Mango","apple"]#List
for j in food:
    print(j)
print(food)
#Tuple
name=("Goldie","Gulshan")
for names in name:
    print(names)
#print even no. skip multiplication value of 3
for i in range(1,21):
    if i%2==0:
        if i%3==0:
            continue#continue statement skip the value and break stop in this value
        print (i)
w=0
while w<=20:
    if w%3==0:
        w +=2
        continue
    print(w)
    w+=2