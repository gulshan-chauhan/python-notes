def average_marks():
    name=input("Enter your name: ")
    print(f"Hello {name} welcome to marks calculator")
    n=int(input("Enter Number of subject:"))
    maximum=int(input("Enter maximum marks : "))
    sums=0
    for i in range(n):
        marks=int(input(f"Enter marks of subject {i+1}: "))
        sums+=marks
    print(f"Total marks of subject is: {sums}")
    maximum= sums/maximum
    maximum=maximum*100
    print(f"Percentage of subject is: {maximum}%")
    if maximum>=90:
        print("Passed with Grade: A")
    elif maximum>=80 and maximum<90:
        print("Passed with Grade: B")
    elif maximum>=70 and maximum<80:
        print("Passed with Grade: C")
    elif maximum>=60 and maximum<70:
        print("Passed with Grade: D")
    else:
        print("Failed")
average_marks()
average_marks()