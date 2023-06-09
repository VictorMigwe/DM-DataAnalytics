#Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5

#Enter a file name: mbox.txt
#zqian@umich.edu 195

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        #print (words)
        counts[words[1]] = counts.get(words[1], 0) + 1
            
print (counts)

maximum = 0

for email in counts:
    if counts[email] > maximum :
        maximum = counts[email]
        best_email = email
        
print (best_email, maximum)
