#Exercise 6.4: There is a string method called count that is similar to the function in the previous exercise. Read the documentation of this method at:
        
#        https://docs.python.org/library/stdtypes.html#string-methods

#Write an invocation that counts the number of times the letter a occurs in “banana”.

#############################################################################

#Here is the relevant portion from that website:

#        str.count(sub[, start[, end]])

#Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.

###############################################################################

word = "Banana"
letter = "a"

word.count(letter)
print(word.count(letter))