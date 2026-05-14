t = (1, 200, 333, 872, 1102, 1467)
print(t.count(200))  # Output: 1 # counts the number of occurrences of the specified element in the tuple
print(t.index(1102))  # Output: 4, as the first occurrence of 1102 is at index 4

# Tuple methods:-
# tuple.count()
# tuple.index()

tuple1 = (1, 2, 3, 4, 5)
slice = tuple1[1:4]  # Slicing the tuple from index 1 to 3 (4 is exclusive)
print(slice)  # Output: (2, 3, 4)

tuple2 = (10, 20, 30, 40, 50)
# Concatenating two tuples
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 10, 20, 30, 40, 50)

tuple3 = (100, 200, 300)
# Repeating a tuple
repeated_tuple = tuple3 * 3
print(repeated_tuple)  # Output: (100, 200, 300, 100, 200, 300, 100, 200, 300)

tuple4 = (1, 2, 3, 4, 5)
# Unpacking a tuple
a, b, c, d, e = tuple4
print(a, b, c, d, e)  # Output: 1 2 3 4 5

tuple5 = (1, 2, 3, 4, 5)
# Checking if an element exists in the tuple
print(3 in tuple5)  # Output: True
print(6 in tuple5)  # Output: False

tuple6 = (1, 2, 3, 4, 5)
# Finding the length of a tuple
print(len(tuple6))  # Output: 5

tuple7 = (1, 2, 3, 4, 5)
# Finding the maximum and minimum values in a tuple
print(max(tuple7))  # Output: 5
print(min(tuple7))  # Output: 1

tuple8 = (1, 2, 3, 4, 5)
# Finding the sum of all elements in a tuple (only works if all elements are numbers)
print(sum(tuple8))  # Output: 15

tuple9 = (1, 2, 3, 4, 5)
# Finding the average of all elements in a tuple (only works if all elements are numbers)
average = sum(tuple9) / len(tuple9)
print(average)  # Output: 3.0
