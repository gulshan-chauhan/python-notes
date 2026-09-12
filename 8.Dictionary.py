# Dictionary is a built-in data type use to store data in key-value pair.It is unordered means no indexing & mutable.Don't allow duplicate key
student={
    "Name":"Goldie",
    "City":"Mandi",
    "age":19,
    "Roll_No.":110
    }# Name is Key & Goldie is value
print(type(student))
print("Your Dictionary:",student)
# Access value by key
print("City:",student["City"])
student["City"]="Chandigarh"# Update value of city
print("Updated City:",student["City"])
student["favsub"]="Python"# Add new key-value
print("Your Dictionary after adding favorite subject:",student)
#Removing item
student.pop("age")
print("Keys in the dictionary:",student.keys())#Return keys