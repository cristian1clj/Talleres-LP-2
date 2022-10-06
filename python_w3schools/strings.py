# Use the len method to print the length of the string.
txt = 'Hello World'
print(len(txt))

# Get the first character of the string txt.
x = txt[0]

# Get the characters from index 2 to index 4 (llo).
x = txt[2:5]

# Return the string without any whitespace at the beginning or the end.
txt2 = ' Hello World '
x = txt2.strip()

# Convert the value of txt to upper case.
txt = txt.upper()

# Convert the value of txt to lower case.
txt = txt.lower()

# Replace the character H with a J.
txt = txt.capitalize()
txt = txt.replace('H', 'J')

# Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = 'My name is John, and I am {}'

print(txt.format(age))