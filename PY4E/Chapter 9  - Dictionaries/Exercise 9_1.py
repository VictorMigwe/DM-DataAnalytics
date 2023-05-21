#Exercise 9.1: Download a copy of the file www.py4e.com/code3/words.txt

#Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

data_file = input("Enter a File Name: ")
fileHandler = open(data_file, 'r')

word_dict = {}

for line in fileHandler:
    words = line.rstrip()
    morewords = words.split()
    
    for moreword in morewords:
        word_dict[moreword] = None
        
print ("would" in word_dict)
print("me" in word_dict)
        