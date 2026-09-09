# Dictionary is a built-in data type use to store data in key-value pair.It is unordered means no indexing & mutable.Don't allow duplicate key
student={
    "Name":"Goldie",
    "City":"Mandi",
    "age":19,
    "Roll_No.":110
    }# Name is Key & Goldie is value
print(type(student))
print(student)
# Access value by key
print(student["City"])
student["City"]="Chandigarh"# Update value of city
print(student["City"])
student["favsub"]="Python"# Add new key-value
print(student)
#Removing item
student.pop("age")
print(student.keys())#Return keys