'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

#Write the necessary code to read a degree in Fahrenheit from the console
temp = input("insert degree in Fahrenheit")
tempintg = int(temp)
#convert it to Celsius and print it to the console.
tempincel = (tempintg - 32) * (5 / 9)
print (tempincel)