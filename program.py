text = 'Hi my name is Zachary!'
for char in text:
  print(char)

# Define a string variable
my_string = "Hello, World!"

# 1. Print the length of the string
print(len(my_string))

# 2. Convert the string to all uppercase
my_string = my_string.upper()

# 3. Print the string in reverse order
print(my_string[::-1])

# 4. Replace all occurrences of the letter "l" with the letter "z"
my_string = my_string.replace("l", "z")

# 5. Split the string into a list of words
words = my_string.split()

# 6. Join the list of words with a hyphen separator
my_string = "-".join(words)

# 7. Add a comma and an exclamation mark to the end of the string
my_string += ",!"

# 8. Remove all whitespace characters from the string
my_string = "".join(my_string.split())

# 9. Check if the string starts with the letter "H"
if my_string.startswith("H"):
    print("The string starts with 'H'")
else:
    print("The string does not start with 'H'")

# 10. Print the final string
print(my_string)
