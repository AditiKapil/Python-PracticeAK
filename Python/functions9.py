def guess_the_number():
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

print(guess_the_number())
       
def hot_or_cold():
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

print(hot_or_could())

def bottles_of_pop():
    for i in range(1,101,1):
        print(i, 'bottles of pop on the wall.')
        print(i, 'bottles of pop.')
        print('If one of those bottles should happen to fall...')
        print('There would be')
        print(i, 'bottles of pop on the wall.')

print(bottles_of_pop())
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     


    
