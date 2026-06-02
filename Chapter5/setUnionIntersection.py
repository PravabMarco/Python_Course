s1 = {1, 2, 3, 4}

s2 = {3, 4, 5, 6}

print(s1.union(s2))  # Output: {1, 2, 3, 4, 5, 6}, as the union of s1 and s2 includes all unique elements from both sets
print(s1.intersection(s2))  # Output: {3, 4}, as the intersection of s1 and s2 includes only the elements that are present in both sets (3 and 4)
print(s1.difference(s2))  # Output: {1, 2}, as the difference of s1 and s2 includes only the elements that are present in s1 but not in s2 (1 and 2)
print(s2.difference(s1))  # Output: {5, 6}, as the difference of s2 and s1 includes only the elements that are present in s2 but not in s1 (5 and 6)