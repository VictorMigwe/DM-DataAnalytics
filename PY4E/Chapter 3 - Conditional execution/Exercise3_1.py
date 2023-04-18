#Exercise 3.1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0


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