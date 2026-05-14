# #program to create student marks and sort it
# studentMarks = [78, 85, 92, 88, 76, 95, 89]
# sortedMarks = sorted(studentMarks)
# print("Sorted Marks:", sortedMarks)

studentMarks = []

s1 = input("Enter the marks of student 1: ")
studentMarks.append(int(s1))
s2 = input("Enter the marks of student 2: ")
studentMarks.append(int(s2))
s3 = input("Enter the marks of student 3: ")
studentMarks.append(int(s3))
s4 = input("Enter the marks of student 4: ")
studentMarks.append(int(s4))
s5 = input("Enter the marks of student 5: ")
studentMarks.append(int(s5))

sortedmarks = sorted(studentMarks)
print("Sorted Marks:", sortedmarks)

# studentMarks.sort() # This will also sort the list in place
# print("Sorted Marks:", studentMarks)