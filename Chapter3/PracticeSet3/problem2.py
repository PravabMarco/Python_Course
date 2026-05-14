#progrtam to fill in the name and date in the letter template
letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''

name = input("Enter your name: ")
date = input("Enter the date: ")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)

# print(letter.replace("<|NAME|>", name)) 
# print(letter.replace("<|DATE|>", date))