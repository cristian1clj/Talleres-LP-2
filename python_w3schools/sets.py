# Check if "apple" is present in the fruits set.
fruits = {'apple', 'banana', 'cherry'}

if 'apple' in fruits:
    print('Yes, apple is a fruit!')

# Use the add method to add "orange" to the fruits set.
fruits.add('orange')

# Use the correct method to add multiple items (more_fruits) to the fruits set.
more_fruits = ["mango", "grapes"]
fruits.update(more_fruits)

# Use the remove method to remove "banana" from the fruits set.
fruits.remove('banana')

# Use the discard method to remove "banana" from the fruits set.
fruits.discard('banana')