marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

print(marks.items())  # Output: dict_items([('Alice', 85), ('Bob', 92), ('Charlie', 78)]    
print(marks.keys())  # Output: dict_keys(['Alice', 'Bob', 'Charlie'])
print(marks.values())  # Output: dict_values([85, 92, 78])
print(marks.update({"Alice": 88, "Eve": 90}))  # Adding multiple key-value pairs using update method
print(marks)  # Output: {'Alice': 88, 'Bob': 92, 'Charlie': 78, 'Eve': 90}
print(marks.get("Alice"))  # Output: 88, using get method to retrieve value for key "Alice"
print(marks.get("Frank"))  # Output: None, using get method with default value for non-existent key "Frank"