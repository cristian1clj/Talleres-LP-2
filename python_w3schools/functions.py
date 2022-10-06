# Create a function named my_function.
def my_function():
    print('Hello from a function')

# Execute a function named my_function.
my_function()


# Inside a function with two parameters, print the first parameter.
def my_function(fname, lname):
    print(fname)


# Let the function return the x parameter + 5.
def my_function(x):
    return x + 5


# If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(*kids):
    print(f'the youngest child is {kids[2]}')


# If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(**kid):
    print('his last name is ' + kid['lname'])