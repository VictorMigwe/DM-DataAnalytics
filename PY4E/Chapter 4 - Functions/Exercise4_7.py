#Exercise 4.7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

# Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
# < 0.6     F

#Enter score: 0.95
#A

#Enter score: perfect
#Bad score

#Enter score: 10.0
#Bad score

#Enter score: 0.75
#C

#Enter score: 0.5
#F

#Run the program repeatedly to test the various different values for input.

error_msg_invalid = "ERROR: Invalid input."

def computegrade(score):
    score = float(score)
    if score < 0.6:
        print ('F')
    #break
    
    elif score >= 0.9:
        print ('A')
    #break
    
    elif score >= 0.8:
        print ('B')
    #break
    
    elif score >= 0.7:
        print('C')
    #break
    
    elif score >= 0.6:
        print('D')
    #break
    
    else:
        print ('wtf?')

input_score = input('Enter a score between 0.0 and 1.0: ')
try:
    if (float(input_score) >= 0) and ( float(input_score) <= 1 ):
        computegrade(input_score)
    #print('valid input, thanks!')
    else:
        print (error_msg_invalid)
    #input_score = raw_input('Enter a score between 0.0 and 1.0: ')
    
except:
    print (error_msg_invalid)
  #input_score = raw_input('Enter a score between 0.0 and 1.0: ')
