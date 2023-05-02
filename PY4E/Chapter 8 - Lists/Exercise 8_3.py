#Exercise 8_3: Rewrite the guardian code in the above example without two if statements. Instead, use a compound logical expression using the or logical operator with a single if statement.

data_file = input("Enter the file name: ")
filehandler = open(data_file, 'r')
count = 0
for line in filehandler:
    words = line.split()
    
    if len(words) == 0 or len(words) < 3 or words[0] != 'From' : continue
    print (words[2])
