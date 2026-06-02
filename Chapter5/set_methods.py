s = {1, 34, 45, 45, 45, 56, 67}

print(s , type(s))  # Output: {1, 34, 45, 56, 67} <class 'set'>, as 's' is a set variable
s.add(78)  # Adding an element to the set using add method
print(s)  # Output: {1, 34, 45, 56, 67, 78}, as 's' now includes the new element 78
s.remove(34)  # Removing an element from the set using remove method
print(s)  # Output: {1, 45, 56, 67, 78}, as 's' no longer includes the element 34
s.discard(45)  # Removing an element from the set using discard method
print(s)  # Output: {1, 56, 67, 78}, as 's' no longer includes the element 45
s.pop()  # Removing and returning an arbitrary element from the set using pop method
print(s)  # Output: {56, 67, 78}, as 's' no longer includes the element 34
s.remove(56)  # Removing a specific element from the set using remove method
print(s)  # Output: {67, 78}, as 's' no longer includes the element 56
s.pop()  # Removing and returning an arbitrary element from the set using pop method
print(s)  # Output: {78}, as 's' no longer includes the element 67