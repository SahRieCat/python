'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
#input
usrinp = input("enter sentence")
#count
print("A/a = ",*map(usrinp.lower().count, "Aa"))
print("E/e = ",*map(usrinp.lower().count, "Ee"))
print("I/i = ",*map(usrinp.lower().count, "Ii"))
print("O/o = ",*map(usrinp.lower().count, "Oo"))
print("U/u = ",*map(usrinp.lower().count, "Uu"))
