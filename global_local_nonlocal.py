marks = 3.95  # Global variable
x = marks
def show():
    print("in the fx", x)  # Can access but not modify without 'global'

show()
print("Outside fx:", x)  # Accessible everywhere


x = 10  

def modify():
    global x  # Now we can modify the global variable
    x = 20

modify()
print("After modification:", x)


#Local
def my_function():
    y = 5  # Local variable
    print("Inside function:", y)
    print(y)

#my_function()
#print("Outside function:", y)  # ERROR! 'y' is not defined outside


def outer_function():
    a = 5  # This is a variable in the outer function (nonlocal to inner_function)

    def inner_function():
        nonlocal a  # Refers to 'a' from the outer function
        a = 10  # Changes the outer function’s variable
        print("Inside inner_function:", a)

    inner_function()
    print("Inside outer_function:", a)  # Value changed in inner function

outer_function()
