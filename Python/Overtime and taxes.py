pay = float(input("Enter in your base pay: "))
hours = int(input("Enter the number of hours you've worked: "))

def salary(pay,hours):
    if pay < 11.40:
        print("Error")
    elif hours > 60:
        print("Error")
    else:
        if hours > 40:
            overtime = pay*1.5
            print("Your overtime is", overtime)

def income_tax(pay, hours):
    if pay <= 1000:
        tax = pay*0.15
        print("Your income tax is", tax)
    
    elif pay > 1000:
        tax_2 = pay*0.20
        print("Your income tax is", tax_2)
        
