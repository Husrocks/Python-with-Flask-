# 1. Dynamic Typing and Reassignment\
num = 10 
print (num , type(num))

#Reassign

num = 10.5
print(num , type(num))

num = "My name is Hussnain"
print(num,type(num))

num = [1,3,5,7,11,13]
print(num, type(num))

num = [88,09.9,"apple", True]
print(num,type(num))
for value in num:
    print (f"values in a list {value}, data type {type(value)}")
#dict
num = {"name ": "Hussnain", "age" : 20}
print(num,type(num))

for value in num:
    print(f"value {value} data type {type(value)}")

# Multiple  Variable Assignment 
cont , cit, sch, clg, uni = "Pakistan","Lahore","Buraq High School", "Concordia College","Institute for art and vulture"
print(cont, cit, sch,uni)

# Swap variables without a temporary variable
a , b , c = 10 , "Hussnain" , 3.6
a, b = b, a
print(a, b)

#unpack the list 
data = ( 1,2,3)
x, y, z = data 
print ( x,y,z)

#unpack the list 
data = [ 4,5,6]
x, y, z = data 
print ( x,y,z)

#Global Variable
num = 10  # This is a global variable

def increase_num():
    global num  
    num += 90   

print(num)  
increase_num()
print(num)  
# num is defined outside the function, so it's a global variable.

