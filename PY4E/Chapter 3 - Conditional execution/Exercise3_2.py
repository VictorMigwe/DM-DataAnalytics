#Exercise 3.2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input


#Enter Hours: forty
#Error, please enter numeric input

try:
    hours = float(input("Enter Hours: "))
    rate = float(input("What is the Rate?: "))

    if hours > 40:
        bonus = (hours-40)*(1.5*rate)
        total_rate = (rate*40)+bonus
        print("Pay: ",total_rate)
        
    else:
        total_rate = rate*hours
        total_rate_str = str(total_rate)
        print("Pay: ", total_rate_str)

except:
    print("Error, please enter numeric input")