#Exercise 6.5: Take the following Python code that stores a string:
        
#        str = 'X-DSPAM-Confidence:0.8475'

#Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.


text = "X-DSPAM-Confidence:    0.8475"

at_position = text.find(":")
print (at_position)
host = text[at_position+1:]
print (float(host))


