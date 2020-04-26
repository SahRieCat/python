'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
#inputname
username = input("what is your name? ")
# moving the first letter to the end
first_letter = username[0]
rest = username [1:]
# followed by "ay"
ends = "ay"

new = (rest)+(first_letter)+(ends)
print(new)