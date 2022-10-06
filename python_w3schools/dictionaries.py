# Use the get method to print the value of the "model" key of the car dictionary.
car = {
    'brand': 'Ford', 
    'model': 'mustang', 
    'year': '1964'
}

print(car.get('model'))

# Change the "year" value from 1964 to 2020.
car['year'] = 2020

# Add the key/value pair "color" : "red" to the car dictionary.
car['color'] = 'red'

# Use the pop method to remove "model" from the car dictionary.
car.pop('model')

# Use the clear method to empty the car dictionary.
car.clear()