# Set is a collection of unordered & unique item.It is mutable
sets={"Burgur","Sandeitch","Paneer"}#Remove 1st paneer
print(type(sets))
sets.add("Pizza")
print(sets)
empty_set=set()
sets.remove("Burgur")
print(sets)
# List into set
lists=["python","Java","C++","python"]
print(type(lists))
print(lists)
sets=set(lists)#converted
print(type(sets))
print("I know language",len(sets))
print(sets)