'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

#String input:
usrsent = input("write a sentence")
#Symbol input:
usrsym = input("insert a symbol")
#the letter we want to replace
fl = usrsent[0]
#Result: #ore python progra##ing pleasen
print(usrsent.replace(fl,usrsym ))
