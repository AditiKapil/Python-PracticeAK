F = int(input("Enter a temperature in Fahrenheit "))
C = (F - 32)*5/9
print("The temperature in Celsius is",C)
h_c = input("Is that hot enough for you?(y/n) ")
if (h_c =='y') and C > 25:
    print("Yes it's hot!")
elif (h_c =='y') and C < 20:
    print("No it's not hot")
elif (h_c =='n') and C > 25:
    print("Something is wrong with your body temperature!")

