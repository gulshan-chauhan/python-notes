# It stores multiple values like a list ,but it is Immutable ,Indexing 0 - n
student_tuple=("Goldie","Gulshan","Goldie")
print(student_tuple[0])
#Empty Tuple
emptyTup=()
print(type(emptyTup))
#Single tuple
single_Tup=(1,)
print(type(single_Tup))
print(student_tuple.index("Goldie"))
print(student_tuple.count("Goldie"))
print(len(student_tuple))
marks=float(input("Enter marks:"))
marks1=float(input("Enter marks 1:"))
marks2=float(input("Enter marks 2:"))
marks3=float(input("Enter marks 3:"))
tup=(marks,marks1,marks2,marks3)
print(max(tup))