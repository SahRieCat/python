'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.


'''
# Convert an int to a float
a = 2
float_a = float(a)
print (float_a)

# Convert a float to an int
b = 2.00
int_b = int(round(b))
print(int_b)

# Perform floor division using a float and an int.
c = a//b
print(c)

# Use two user inputted values to perform multiplication.
user_age = input("how old are you? ")
age = int(user_age)
user_hight = input("what is your hight? ")
hight = float(user_hight)
multi = age*hight
print("user age*hight = ",multi, "cm")