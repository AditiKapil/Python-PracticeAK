## Aditi Kapil ##
## Haunted House ##

## The list of all the weapons
laundry_weapons = ["Sword(s), Invisibility cape(c), for both(sc)"]
storage_weapons = ["Shield(sh), Blow horn(b), for both (shb)"]
bathroom_weapons = ["Soap(so)"]
your_weapons = []

## All my functions for the game
def kitchen():
        print("\t The kitchen is very old fashioned, straight from the 90's. The furniture and most appliances are very old and worn down. \n Mold and a variety of different insects are spotted in the randomness locations around the kitchen, this pretty much states that the kitchen hasn't been used in a very long time!\n I wonder if any of the applications work as well? Why not give it a go? Besides, you can let the clown try some as well!")
def dining_room():
        print("\t You obviously need a place to eat your amazingly delicious food that you’ve created from the kitchen.\n Welcome to the dining room, aka the only room where you can eat and leave the most utter less uselessness on the planet!\n For instance, you’d probably end up using 30% of the room for eating. The rest would be used as storage space!")
def living_room():
        print("\t You’re probably thinking that there must be nothing haunted in a living room, because it’s a place where guests can relax and feel welcomed…AHAH!\n I lied! Just like the rest of the house it’s haunted to the very edge of every single room.\n Oh I almost forgot! Just be careful as it has been a while since this place has been cleaned up.")
def bathroom():
        print("\t Surprisingly the bathrooms are fairly clean and sanitary as compared to any of the rooms in this house.\n Of course we needed to keep the restrooms clean for sanitary sakes,\n but what if there was another reason why?")
def laundry():
        print("\t AH! The smell of clean clothes coming straight out of the laundry is one very satisfying sent.\n Luckily, for you there are two special weapons in this room that you can use to defeat\n and destroy the many perils that might come in your way.")
def storage():
        print("\t Honestly, there isn’t really much to say about this room than what it’s really used for. STORAGE!....\n BUUUTTT there are special equipment inside that might help you in case you get attacked\n by one of the monsters in this house.")
def parents_room():
        print("\t A very antique master bedroom with high class furnishings from very expensive wood found in the forests\n of the northern Canadian Shield. Everything was neat and tidy before the attack, however you can tell\n that it’s been haunted by both parents because from time to time some of the items inside the room with move from place to place!\n Pretty creepy huh!!!")
def twins_room():
        print("\t The twin’s that used to sleep here were a crazy yet fun bunch. The oldest twin is a girl and she was 2 minutes earlier than her twin brother.\n Also, surprisingly enough that was the exact same time difference between both twins when they died! Coincidence?\n Any who, their room is compiled with a bunkbed, two desks, a play area, and two full length closets for each one.\n But of course to know which was who’s the items were colour coded as blue for the brother and red for the sister.")
def brothers_room():
        print("\t The older brother’s room is a crazy mess! Just like every other teenager’s bedroom, it looks like a never ending maze of clothes, books, games, and other things!\n He did however had his bed done right before he was reportedly shot at the back of his head. No wonder there’s blood stains all over his white bedsheet.\n You can try going into his room but the chances of you leaving due to how messy the floor is will be very high. Good Luck!")
def main_room():
        print("\t Welcome to the main room!\n There really isn't much to do here besides leaving the haunted house or acctually going in.\n So are you up for the challenge or no?")
def female_ghost():
        print("  ___ ")
        print(" (| |)")       
        print(" (   )")           
        print(" /   \ ")
        print(" |___| ")
def male_ghost():
        print(" ___")
        print("{| |}")
        print("(   )")          
        print("|   |")
        print("|___|")
def dust_bunny():
        print("    _____ ")
        print("   (     )")
        print("  (       )")
        print(" (        )")
        print("(   0 0    )")
        print(" (        )")
        print(" ( \---/ )")
        print("  (_____)")

## Begining of my program    
print("Welcome to the Haunted House of the Harris'!")
print()
enter = input("Do you have the guts to enter this horrifying, yet mysterious looking house? (y/n)")
if enter=='y':
        print("\tThe Harris' were a family of 5 whom used to live in this exact home 25 years ago.\nIt all ended when the family died from an unknown suspect whom decided to enter the house and call fire to all members of the family...\nHowever since their death, there have been some remains and some of their belongings inside this house. Rumor has it that their souls are still roaming around in readiness to haunt other visitors who come to the house...\nNo wonder it's haunted!")
elif enter=='n':
        print("What! You chickened out?")
        exit()

## Lower level of the house ##
        
## Main room or entrance to game
print()
direc = input("You have a choice as to where you would like to go. You can go either left, right, or up. Which way would you like to go? (l,r,u) ")
if direc =='l':
        dining_room()
elif direc == 'r':
        living_room()
elif direc == 'u':
        storage()
else:
        print("Uh oh! GAME OVER!!!")
        exit()
        
## Living room
print()
print("There is a big evil dust bunny on the loose in the living room!\n I guess I should've kept this place clean.\n Now I know, I know, dust bunny’s are just little balls of dust nothing to worry about right?\n SIKEEEE! I lied! These bastards a HUGE! Now you’ll see why they’re a threat!\n If you've already been in the laundry room, storage room, or bathroom you would've found some weapons in order to defeat this big ball.\n You could use the sword, invisibility cape, shield, blow horn, or soap?")
dust_bunny()
living = input ("Choose a weapon {0}.".format(your_weapons))
if living == 's':
        print("A sword wouldn't work? The bunny is made out of dust so it won't bleed out anything")
elif living == 'c':
        print("You will be invisable but it will keep on coming back everytime you enter the living room")
elif living == 'sh':
        print("A sheild isn't gonna protect you from anything my friend! The ball is made out of dust god damn it!")
elif living == 'b':
        print("You'll make a lot of noise....but it's not like the dust bunny has any ears?")
elif living == 'so':
        direc2 = input("Yeah! You defeated the dust bunny by cleaning it up until it got so small that it disappeared!\n which way do you want to go now? Do you want to go forwards or backwards? (f,b)")
        if direc2 == 'f':
                laundry()
        elif direc2 == 'b':
                main_room()
else:
        print("You didn't gather any weapons to protect yourself? Your dead my friend")
        exit()
## Dining room
print()
dining = input("Thankfully, there aren't any perils in this room.\n where would you like to go? Would you like to go forwards, backwards, or right?\n (f,b,r)")
if dining == 'f':
        storage()
elif dining == 'b':
        main_room()
elif dining == 'r':
        kitchen()
else:
        print("There is no where else to go...\n Game Over")
        exit()

## Storage 1
print()
storage_1 = input("The weapons availalbe in this room are a sheild, and a blow horn.\n You can pick up both or just one, your choice.\n You can also just simply leave if you like. (sh,b,shb,leave) ")
if storage_1 == 'sh':
        your_weapons.append("sheild")
elif storage_1 == 'b':
        your_weapons.append("blow horn")
elif storage_1 == 'shb':
        your_weapons.append("sheild")
        your_weapons.append("blow horn")
elif storage_1 == 'leave':
        direc3 = input("Well that sucks, you should've gotten some weapons.\n Where would you like to go? forwards, right, or upstairs onto the second level? (f,r,u) ")
        if direc3 == 'f':
                kitchen()
        elif direc3 == 'r':
                laundry()
        elif direc3 == 'u':
                bathroom()
else:
        print("Game Over...")
        exit()

## Storage 2
print()
storage_2 = input("The weapons availalbe in this room are a sheild, and a blow horn.\n You can pick up both or just one, your choice.\n You can also just simply leave if you like. (sh,b,shb,leave) ")
if storage_2 == 'sh':
        your_weapons.append("sheild")
elif storage_2 == 'b':
        your_weapons.append("blow horn")
elif storage_2 == 'shb':
        your_weapons.append("sheild")
        your_weapons.append("blow horn")
elif storage_2 == 'leave':
        direc6 = input("Well that sucks, you should've gotten some weapons.\n Where would you like to go? south, or east? (s,e) ")
        if direc6 == 's':
                dining_room()
        elif direc6 == 'e':
                bathroom()
else:
        print("Game Over...")
        exit()
        
## laundry room
print()
laundry = input("The weapons available in this room are a sword, an invisability cape, or both?\n You could just simply leave. (s,c,sc,leave) ")
if laundry == 's':
        your_weapons.append("sword")
elif laundry == 'c':
        your_weapons.append("invisability cape")
elif laundry == 'sc':
        your_weapons.append("sword")
        your_weapons.append("invisability cape")
elif laundry == 'leave':
        direc4 = input("Your going to leave without any weapons? Have fun diying then I guess...\n Where would you like to go? You can go either back, north-left, left, or south-left. (b,nl,l,sl) ")
        if direc4 == 'b':
                living_room() 
        elif direc4 == 'nl':
                bathroom()
        elif direc4 == 'l':
                kitchen()
        elif direc4 == 'sl':
                storage()
else:
        print("Game Over...Bye, bye!")
        exit()

## Kitchen
print()
print("Killer clowns…You know the ones that were suppose to bring joy and happiness to many people.\n Oh my bad! I was refering to just clowns. Anywho, recently there has been a change to that.\n Please welcome the killer clowns! Besides being a great source of entertainment, they’re now known as source of fear and cruelty.\n However when in doubt, use an instrument that can make LOUD sounds and is very annoying to many people, including killer clowns.\n Are you thinking of what I'm thinking? Just make sure to hold the instrument for at least 10 seconds.\n You could use the sword, invisibility cape, shield, blow horn, or soap?")
kit = input ("Choose a weapon {0}.".format(your_weapons))
if kit == 's':
        print("Sword would work...If only the killer clown didn't have any weapons on him to begin with")
elif kit == 'c':
        print("You will be invisable but it won't last long enough for you to escape")
elif kit == 'sh':
        print("A sheild isn't gonna protect you from anything pal! It's a killer clown bro, his ears are the only weakest thing")
elif kit == 'b':
        direc5 = input("Yeah! You defeated the killer clown!\n which way do you want to go now? Do you want to go forwards, backwards, right, or left (f,b,r,l)")
        if direc5 == 'f':
                bathroom()
        elif direc5 == 'b':
                storage()
        elif direc5 == 'r':
                laundry()
        elif direc5 == 'l':
                dining_room() 
        
elif kit == 'so':
        print("Yeah you could use the soap for the clown to slip on, but I don't think it makes any noise")
else:
        print("You didn't gather any weapons to protect yourself? Your dead my friend")

## Bathroom 1
print()
bath_1 = input("The weapons available in this room is only soap and that's it!\n You can get that of just simply leave. (so,leave) ")
if bath_1 == 'so':
        your_weapons.append("soap")
elif bath_1 == 'leave':
        direc7 = input("Which way would you like to go?\n Do you want to go left, right, or south? (l,r,s) ")
        if direc7 == 'l':
                storage()
        elif direc7 == 'r':
                laundry()
        elif direc7 == 's':
                kitchen()
else:
        print("Game Over!")
        exit()


## Upper Level of Haunted House ##

## Bathroom #2
print()
bath_2 = input("The weapons available in this room is only soap and that's it!\n You can get that of just simply leave. (so,leave) ")
if bath_2 == 'so':
        your_weapons.append("soap")
elif bath_2 == 'leave':
        direc8 = input("Which way would you like to go?\n Do you want to go back downstairs, north, south, or right? (d,n,s,r) ")
        if direc8 == 'd':
                storage()
        elif direc8 == 'n':
                brothers_room()
        elif direc8 == 's':
                twins_room()
        elif direc8 == 'r':
                parents_room()
else:
        print("Game Over!")
        exit()

## Bathroom #3
print()
bath_3 = input("The weapons available in this room is only soap and that's it!\n You can get that of just simply leave. (so,leave) ")
if bath_3 == 'so':
        your_weapons.append("soap")
elif bath_3 == 'leave':
        direc9 = input("Which way would you like to go?\n Do you want to go left, or right? (l,r) ")
        if direc9 == 'l':
                brothers_room()
        elif direc9 == 'r':
                parents_room()
else:
        print("Game Over!")
        exit()

## Brother's Bedroom
print()
print("The evil brother ghost is just like any other teenaged ghost. He tends to give a lot of attitude and will always get what he demands,\n Although, one of his weakest points is his huge collection of PumkiMon Cards. If you dare try and destroy them, He will disappear forever!\n If you've already been in the laundry room, storage room, or bathroom you would've found some weapons in order to defeat this ghost.\n You could use the sword, invisibility cape, shield, blow horn, or soap?")
male_ghost()
bro = input ("Choose a weapon {0}.".format(your_weapons))
if bro == 's':
       direc10 = input("Yeah! You defeated the brother ghost!\n Which way do you want to go now? Do you want to go downstairs, or right? (d,r)")
       if direc10 == 'd':
                storage()
       elif direc10 == 'r':
                bath_room()
elif bro == 'c':
        print("You will be invisable but it really won't help you. ")
elif bro == 'sh':
        print("A sheild will protect you but it won't let you destroy the most valuable collection of PumkiMon Cards.")
elif bro == 'b':
        print("The brother ghost really loves music...He's a teenager after all.")
elif bro == 'so':
        print("Soap? To destroy cards? I don't think so.")
else:
        print("You didn't gather any weapons to protect yourself? Your dead my friend")
        exit()
## Parent's Bedroom
print()
print("Parent ghosts…The most annoying and deadly from them all! Both parents only go by their well known but very strong power, and that is to throw gigantic fire balls! Fuming in huge flames, the fire balls are half fire, and half molten rock!!!\n If you've already been in the laundry room, storage room, or bathroom you would've found some weapons in order to defeat this ghost.\n You could use the sword, invisibility cape, shield, blow horn, or soap?")
male_ghost()
female_ghost()
parent = input ("Choose a weapon {0}.".format(your_weapons))
if parent == 's':
        print("A sword isn't going to help you when your going against gigantic fire balls.")
elif parent =='c':
        print("You can be invisable but the heat of the fire ball is too strong and csn still burn you up")
elif parent == 'sh':
        direc11 = input("You've defeated the two parent ghosts!\n Which way do you want to go now? Do you want to go west, or south-west? (w,sw) ")
        if direc11 == 'w':
                bathroom()
        elif direc11 == 'ws':
                twins_room()
elif parent == 'b':
        print("Blow horns! It's just going to make them even more upset!")
elif parent == 'so':
        print("Soap? Lollllll thats so funny")
else:
        print("You didin't gather any weapons to protect your self? Well have fun dying")
        exit()

## Twin's Bedroom
print()
print("The evil twin ghosts are no ordinary pair of twins.\n They are way more deadly than you think. Trying to outrun them will never work since they are both telepathic thus making is almost impossible for you to make it through! What will you do?\n If you've already been in the laundry room, storage room, or bathroom you would've found some weapons in order to defeat this ghost.\n You could use the sword, invisibility cape, shield, blow horn, or soap?")
male_ghost()
female_ghost()
twins = input ("Choose a weapon {0}.".format(your_weapons))
if twins == 's':
        print("A sword isn't going to help you when your going against ghosts.")
elif twins =='c':
        direc12 = input("You've defeated the evil twin ghosts!\n Which way do you want to go now? Do you want to go north or do you wanna go downstairs? (n,d) ")
        if direc12 == 'n':
                storage()
        elif direc12 == 'd':
                bathroom()
elif twins == 'sh':
        print("The ghosts are gonna go through your sheild and attack you!")
elif twins == 'b':
        print("Blow horns! Really?")
elif twins == 'so':
        print("Soap? i dont't think so....")
else:
        print("You didin't gather any weapons to protect your self? Well have fun dying")
        exit()



        
