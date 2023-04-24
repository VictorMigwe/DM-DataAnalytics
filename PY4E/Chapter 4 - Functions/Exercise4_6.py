#Exercise 4.6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
#    Enter Hours: 45
#    Enter Rate: 10
#    Pay: 475.0

hours = float(input("Enter Hours: "))
rate = float(input("What is the Rate?: "))

def computepay(hours, rate):    
    if hours > 40:
        extra_time = hours - 40
        return 40 * rate + extra_time * 1.5 * rate

    elif hours < 0: 
        print("Error! Please enter a Numeric Input")
    
    else:
        return hours*rate
        
pay = computepay(hours, rate)    
print("Pay",pay)    