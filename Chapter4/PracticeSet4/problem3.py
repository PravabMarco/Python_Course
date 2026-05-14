#program to demonstrate the immutability of tuples and mutability of lists
# checkList = [1, 2, 3, 4, 5]
# print(type(checkList))  # Output: <class 'list'>
# checkList[0] = 10  # Replace the first element with 10
# print(checkList)  # Output: [10, 2, 3, 4, 5]

#program to demonstrate the immutability of tuples/cannot be changed after creation
a = (10, 20, 30, "Hello")
a[2] = 100  # This will raise a TypeError because 'a' is a tuple and does not support item assignment
print(type(a)) # Output: <class 'tuple'>, as 'a' is now a tuple variable
# a.replace(10, 100) # This will not work as 'a' is a tuple and does not have the 'replace' method
print(a) # Output: (10, 20, 30, "Hello"), as 'a' remains unchanged because the 'replace' method is not available for tuples