#For Loop Programming

#1 - 1)	Count by 2s from 1 to 21. Print the numbers
print()
print("#1")
print()
for a in range(1,22,2):
    print(a)

#2 - 2)	Count by 3’s from 7 to 27. Print the numbers divided by 2
print()
print("\n#2")
print()
for b in range(7,28,3):
    b=b/2
    print(b)

#3 - 3)	Count from 10 to 5. Print the number squared
print()
print("\n#3")
print()
for c in range(10,4,-1):
    print(c*c)
    
#4 - Print lucky numbers
print()
print("\n#4")
print()
counter=0
for i in [2,10,15,5,30,1]:
    counter=counter+1
    print("Lucky number",counter,"is", i)
      
#5 - Print a list of all the values of Canadian bills
print()
print("\n#5")
print()
for d in [5,10,20,50,100]:
    print("Canada has a $"+str(d),"dollar bill.") 

#6 - List each letter in “Turner Fenton”
print()
print("\n#6")
print()
for m in "Turner Fenton":
    print(m)

#7 - Sum all the numbers from 1 to 100
print()
print("\n#7")
print()
total=0
for x in range(1,101):
    total=total+x
print(total)

       
#8 - Average all the odd numbers between 0 and 50
print()
print("\n#8")
print()
total=0
counter=0
for z in range(1,51,2):
    total=total+z
    counter=counter+1
print(total/counter)

#9 - Loop from 1 to 10, but don’t print any numbers divisible by 3
print()
print("\n#9")
print()
for i in range(1,11):
    if i%3!=0:
        print(i)
        
#10 - Print the letters in “But I don’t want to” backwards
print()
print("\n#10")
print()
for w in reversed("But I dont't want to"):
    print(w)
