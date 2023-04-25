#Exercise 5.2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

largest = None
smallest= None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        numint = int(num)
        if smallest is None:
            smallest = numint
        elif numint < smallest:
            smallest = numint
        
        if largest is None:
            largest = numint
        elif numint > largest:
            largest = numint
        
    except:
        print("Invalid input")
    continue
print("Maximum is: ",largest)
print("Minimum is: ",smallest)
        
