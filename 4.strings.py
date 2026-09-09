strl1='Hello'
strl2="Gulshan"
strl3='''Chauhan'''
print(strl1)
#String concatenation
print(strl1+' '+strl2+" "+strl3)

#Length of string
print(len(strl3))#7

#Indexing starting from 0 in string
print(strl1[0])#H

#Slicing :Access part of a string [1st index:end index]End index excluded
print(strl2[3:7])#shan

#Negative indexing
strl="Goldie chauhan"
print(strl[-6:-1])#Goldie

#Formated String
age=int(input("Enter your age:"))
print(f"My name is {strl2+" "+strl3} & I am {age} year old.")

#Escape Sequence
print("Hello\tWorld")
print("Hello\nWorld")

#String Methods
print(strl.upper())
print(strl.lower())
print(strl.title())
print(strl.find("d"))
print(strl.replace("Goldie","Gulshan"))
print(strl.count("a"))#count the occurence