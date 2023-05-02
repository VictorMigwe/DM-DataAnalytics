#fhand = open('mbox-short.txt')
#count = 0
#for line in fhand:
#    words = line.split()
#    # print('Debug:', words)
#    if len(words) == 0 : continue
#    if words[0] != 'From' : continue
#    print(words[2])
    
#Exercise 8_2: Figure out which line of the above program is still not properly guarded. See if you can construct a text file which causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure it handles your new text file.

data_file = input("enter a file: ")
fhand = open(data_file, 'r')
count = 0
for line in fhand:
    words = line.split()
    
    if len(words)== 0: continue
    if words[0] !='From' : continue
    print("Debug:" , words)
    print(words[2])

    
#An error can be included if there's a line starting with "From" and then there's nothing else in the said line.

#This can be guarded (a guardian code) against by using an "or" and making sure the line contains atleast 3 items like shown in the following.


data_file = input("Enter a file name: ")
fileHandle = open(data_file, 'r')
count = 0
for line in fileHandle:
    words = line.split()
    
    if len(words) == 0 or len(words) < 3 : continue
    if words[0] != "From" : continue
    print ("debug:", words)
    print (words[2])