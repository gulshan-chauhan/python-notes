#Assignment 2.0> Take string input & print middle 3 character , last 2 character
st=input("ENTER Character:")
print(len(st))
mid=len(st)//2
output=st[mid-1:mid+2]
print("The middle three character are:",output)#print middle 3 char
output2=st[-2:]#print last 2 char Negative indexing
print("String last two charcter is:",output2)
#Assignment 2.1>print the first char ,middle char & last char & total no. of char
print("String first chatracter is:",st[0])
print("String Middle character is:",st[mid])
print("String last chatracter is:",st[-1:])#Negative indexing

#Assignment 2.2>Emoji converter
msg=input("Enter your message:")
msg=msg.replace(":)","😊")
msg=msg.replace(":(","😒")
msg=msg.replace(":D","😁")
print(msg)