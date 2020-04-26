'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
#input1
usr1 = input("type something")
#input2
usr2 = input("type something")
#input3
usr3 = input("type something")
#count1
cou1 = (len(usr1))

#count2
cou2 = (len(usr2))
#count3
cou3 = (len(usr3))
#printall
print(cou1,",",usr1)
print(cou2,",",usr2)
print(cou3,",",usr3)


#print only the string with the most characters


if cou1 >= cou2:
   print(usr1)
elif cou1 >= cou3:
       print(usr1)

elif cou2 >= cou3:
       print(usr2)
else:
   print(usr3)


