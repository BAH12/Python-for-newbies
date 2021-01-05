                            PYTHON NUMBERS
There are three numeric types in Python
int, float, complex

Variables of numeric types are created when you assign a value to them
x = 1       # int
y = 2.8     # float
z = 1j      # complex

To verify the type of any object in Python,use the type() function
print(type(x))
print(type(y))
print(type(z))

                                INT
Int or integer is a whole number positive or negative without decimals of unlimited lengths
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


                                 FLOAT
Float or floating point number is a number positive or negative containing one or more decimals
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

float can also be scientific numbers with an 'e' to indicate the power of 10
x = 35e3
y = 12E4
z = -87.7e100 

print(type(x))
print(type(y))
print(type(z))



                                    COMPLEX
Complex numbers are written with a 'j' as the imaginary part
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


                                TYPE CONVERSION
You can convert from one type to another with the int(), float(), complex() method
convert from one type to another
x = 1       # int
y = 2.8     # float
z = 1j      # complex

convert from int to float
a = float(x)

convert from float to int
b = int(y)

convert from int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

NOTE: You cannot convert complex numbers into another number type 


                                    RANDOM NUMBER
Python does not have a random() function to make a random number, but python has a built-in module called 'random' that can be used to make random numbers

import the random module and display a random number between 1 and 10

import random
a = random.randrange(1, 11)
print(a)