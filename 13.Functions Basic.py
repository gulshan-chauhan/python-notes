#Function in Python With no argument (Comment selection: Ctrl + K then Ctrl + CUncomment selection: Ctrl + K then Ctrl + U)
def fun():
    print("Hello, I am a function")
fun()
#Function Defination With Parameter
def showName_age(name="goldi",age=19):
    print(f"Hello {name} your age is {age}")
showName_age("Gulshan", 19) 
def fav_food(food):
    print(f"My favourite food is {food}")
fav_food("Pizza")

# Return Statement in Function
def multiply(a=10,b=5):
    return a*b
result=multiply(10,5)
print(result)

#Write a function square(a) that return a sequare of a number. 
def square(a=2):
    return a**2
result=square(5)
print(f"Square of number is: {result}")

#Write a function that take a string and returns the count of vowels & consonants separately.
def fun(userInput):
    #Define vowels and consonants
    vowels="aeiouAEIOU"
    countVowels=0
    countConsonants=0
    for eachChar in userInput:
        if (eachChar.isalpha()):
            if (eachChar in vowels):
                countVowels+=1
            else:
                countConsonants+=1
    return countVowels, countConsonants
#Function call
vowels, consonants=fun("Hello World")
print(f"Vowels: {vowels}, Consonants: {consonants}")

#create a program using global keyboard to modify a variable from inside a function
x = 10
print ("Before:",x)

def change():
    global x
    x = 20

change()

print("After:",x)