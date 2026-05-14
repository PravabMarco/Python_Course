#replacing double space from problem3 with underscore
name = "I am  Prabhav and I am learning Python"
print(name.find("  "))
print(name.replace("  ", "_"))

print(name)#the original string is not changed because strings are immutable in python