#Exercise 6.1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

name = "Victor T. Migwe"
index = len(name)-1
i=0

while i < len(name):
    letter=name[index]
    print (letter)
    index -= 1
    i += 1