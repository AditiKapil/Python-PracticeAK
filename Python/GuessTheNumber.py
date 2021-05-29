import random
x = (random.randint(1,1000))
num = x
while num==x:
    guess=int(input("Guess a number:"))
    if guess==x:
        print("Wow congrats! You got the right number!")
    elif guess==0:
        num = 0
        print("You gave up so quickly? Game over!")
    elif guess>=x:
        print("Your number is way too high! Guess again")
    elif guess<=x:
        print("You number is too low! Guess again")
       
        
