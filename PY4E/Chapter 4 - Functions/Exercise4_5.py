#Exercise 4.5: What will the following Python program print out?
#    a) Zap ABC jane fred jane
#    b) Zap ABC Zap
#    c) ABC Zap jane
#    d) ABC Zap ABC
#    e) Zap Zap Zap

def fred():
   print("Zap")

def jane():
   print("ABC")

jane()
fred()
jane()




# Will print "ABC Zap ABC"