'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
#input1
usrsent = input("enter your sentence")
#input2
usrltr = input("enter a letter")
#find
print(usrsent.find(usrltr))