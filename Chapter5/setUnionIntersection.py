s1 = {1, 2, 3, 4}

s2 = {3, 4, 5, 6}

print(s1.union(s2))  # Output: {1, 2, 3, 4, 5, 6}, as the union of s1 and s2 includes all unique elements from both sets
print(s1.intersection(s2))  # Output: {3, 4}, as the intersection of s1 and s2 includes only the elements that are present in both sets (3 and 4)
print(s1.difference(s2))  # Output: {1, 2}, as the difference of s1 and s2 includes only the elements that are present in s1 but not in s2 (1 and 2)
print(s2.difference(s1))  # Output: {5, 6}, as the difference of s2 and s1 includes only the elements that are present in s2 but not in s1 (5 and 6)
print(s1.symmetric_difference(s2))  # Output: {1, 2, 5, 6}, as the symmetric difference of s1 and s2 includes only the elements that are present in either s1 or s2 but not in both (1, 2, 5, and 6)
print(s1.isdisjoint(s2))  # Output: False, as s1 and s2 are not disjoint sets since they have common elements (3 and 4)
print(s1.issubset(s2))  # Output: False, as s1 is not a subset of s2 since it contains elements (1 and 2) that are not present in s2
print(s1.issuperset(s2))  # Output: False, as s1 is not a superset of s2 since it does not contain all elements of s2 (5 and 6 are missing in s1)
print(s1.clear())  # Output: None, as the clear method removes all elements from s1 and returns None