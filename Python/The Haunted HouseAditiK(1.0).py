## Aditi Kapil ##
## Haunted House ##

## The list of all the weapons
laundry_weapons = ["Sword(s), Invisibility cape(c), for both(sc)"]
storage_weapons = ["Shield(sh), Blow horn(b), for both (shb)"]
bathroom_weapons = ["Soap(so)"]
your_weapons = []

## All my functions for the game
def kitchen():
        print("\t The kitchen is very old fashioned, straight from the 90's. The furniture and most appliances are very old and worn down. \n Mold and a variety of different insects are spotted in the randomness locations around the kitchen, this pretty much states that the kitchen hasn't been used in a very long time!\n I wonder if any of the appliances do work? Why not give it a go? Besides, you can let the clown try some as well!")
        print()
        print("Killer clowns…You know the ones that were suppose to bring joy and happiness to many people.\n Oh my bad! I was referring to just clowns. Anywho, recently there has been a change to that.\n Please welcome the killer clowns! Besides being a great source of entertainment, they’re now known as source of fear and cruelty.\n However when in doubt, use an instrument that can make LOUD sounds and is very annoying to many people, including killer clowns.\n You could use the sword, invisibility cape, shield, blow horn, or soap.")
        killer_clown()
        kit = input ("Choose a weapon {0}[Sword(s), Invisibility cape(c), Shield(sh), Blow horn(b), Soap(so)]​.".format(your_weapons))
        if kit == 's':
                print("Sword would work...If only the killer clown didn't have any weapons on him to begin with!")
                exit()
        elif kit == 'c':
                print("You will be invisible but it won't last long enough for you to escape")
                exit()
        elif kit == 'sh':
                print("A shield isn't gonna protect you from anything pal! It's a killer clown bro, his ears are the only weakest thing")
                exit()
        elif kit == 'b':
                direc14 = input("Yeah! You defeated the killer clown!\n which way do you want to go now? Do you want to go forwards, backwards, right, or left (f,b,r,l)")
                if direc14 == 'f':
                        bathroom_1()
                elif direc14 == 'b':
                        storage_1()
                elif direc14 == 'r':
                        laundry()
                elif direc14 == 'l':
                        dining_room() 
        
        elif kit == 'so':
                print("Yeah you could use the soap for the clown to slip on, but I don't think it makes any noise")
                exit()
        else:
                print("Game Over!")
                exit()
        
def dining_room():
        print("\t You obviously need a place to eat your amazingly delicious food that you’ve created from the kitchen.\n Welcome to the dining room, aka the only room where you can eat and leave the most utter less uselessness on the planet!\n For instance, you’d probably end up using 30% of the room for eating. The rest would be used as storage space!")
        print()
        dining = input("Thankfully, there aren't any perils in this room.\n where would you like to go? Would you like to go forwards, backwards, or right?\n (f,b,r)")
        if dining == 'f':
                storage_2()
        elif dining == 'b':
                main_room()
        elif dining == 'r':
                kitchen()
        else:
                print("There is no where else to go...\n Game Over!")
                exit()
        
def living_room():
        print("\t You’re probably thinking that there must be nothing haunted in a living room, because it’s a place where guests can relax and feel welcomed…\n AHAH! I lied! Just like the rest of the house it’s haunted to the very edge of every single room.\n Oh I almost forgot! Just be careful as it has been a while since this place has been cleaned up.")
        print()
        print("There is a big evil dust bunny on the loose in the living room!\n I guess I should've kept this place clean.\n Now I know, I know, dust bunny’s are just little balls of dust nothing to worry about right?\n SIKEEEE! I lied! These bastards a HUGE! Now you’ll see why they’re a threat!\n If you've already been in the laundry room, storage room, or bathroom you would've found some weapons in order to defeat this big ball.\n You could use the sword, invisibility cape, shield, blow horn, or soap.")
        dust_bunny()
        living = input ("Choose a weapon {0}[Sword(s), Invisibility cape(c), Shield(sh), Blow horn(b), Soap(so)]​.".format(your_weapons))
        if living == 's':
                print("A sword wouldn't work? The bunny is made out of dust so it won't bleed out anything")
                exit()
        elif living == 'c':
                print("You will be invisable but it will keep on coming back everytime you enter the living room")
                exit()
        elif living == 'sh':
                print("A sheild isn't gonna protect you from anything my friend! The ball is made out of dust god damn it!")
                exit()
        elif living == 'b':
                print("You'll make a lot of noise....but it's not like the dust bunny has any ears?")
                exit()
        elif living == 'so':
                direc2 = input("Yeah! You defeated the dust bunny by cleaning it up until it got so small that it disappeared!\n which way do you want to go now? Do you want to go forwards or backwards? (f,b)")
                if direc2 == 'f':
                        laundry()
                elif direc2 == 'b':
                        main_room()
        else:
                print("Game Over!")
                exit()
        
def bathroom_1():
        print("\t Surprisingly the bathrooms are fairly clean and sanitary as compared to any of the rooms in this house.\n Of course we needed to keep the restrooms clean for sanitary sakes,\n but what if there was another reason why?")
        print()
        bath_1 = input("The weapons available in this room is only soap and that's it!\n You can get that of just simply leave. (so,leave) ")
        if bath_1 == 'so':
                your_weapons.append("soap")
                direc7 = input("Which way would you like to go?\n Do you want to go left, right, or south? (l,r,s) ")
                if direc7 == 'l':
                        storage_2()
                elif direc7 == 'r':
                        laundry()
                elif direc7 == 's':
                        kitchen()
        elif bath_1 == 'leave':
                direc7 = input("Which way would you like to go?\n Do you want to go left, right, or south? (l,r,s) ")
                if direc7 == 'l':
                        storage_2()
                elif direc7 == 'r':
                        laundry()
                elif direc7 == 's':
                        kitchen()
        else:
                exit()
        
def bathroom_2():
        print("\t Surprisingly the bathrooms are fairly clean and sanitary as compared to any of the rooms in this house.\n Of course we needed to keep the restrooms clean for sanitary sakes,\n but what if there was another reason why?")
        print()
        bath_2 = input("The weapons available in this room is only soap and that's it!\n You can get that of just simply leave. (so,leave) ")
        if bath_2 == 'so':
                your_weapons.append("soap")
                direc8 = input("Which way would you like to go?\n Do you want to go back downstairs, north, south, or right? (d,n,s,r) ")
                if direc8 == 'd':
                        storage_1()
                elif direc8 == 'n':
                        brothers_room()
                elif direc8 == 's':
                        twins_room()
                elif direc8 == 'r':
                        parents_room()
        elif bath_2 == 'leave':
                direc8 = input("Which way would you like to go?\n Do you want to go back downstairs, north, south, or right? (d,n,s,r) ")
                if direc8 == 'd':
                        storage_1()
                elif direc8 == 'n':
                        brothers_room()
                elif direc8 == 's':
                        twins_room()
                elif direc8 == 'r':
                        parents_room()
        else:
                exit()
        
def bathroom_3():
        print("\t Surprisingly the bathrooms are fairly clean and sanitary as compared to any of the rooms in this house.\n Of course we needed to keep the restrooms clean for sanitary sakes,\n but what if there was another reason why?")
        print()
        bath_3 = input("The weapons available in this room is only soap and that's it!\n You can get that of just simply leave. (so,leave) ")
        if bath_3 == 'so':
                your_weapons.append("soap")
        direc9 = input("Which way would you like to go?\n Do you want to go left, or right? (l,r) ")
        if direc9 == 'l':
                brothers_room()
        elif direc9 == 'r':
                parents_room()
        elif bath_3 == 'leave':
                direc9 = input("Which way would you like to go?\n Do you want to go left, or right? (l,r) ")
        if direc9 == 'l':
                brothers_room()
        elif direc9 == 'r':
                parents_room()
        else:
                exit()
        
def laundry():
        print("\t AH! The smell of clean clothes coming straight out of the laundry is one very satisfying sent.\n Luckily, for you there are two special weapons in this room that you can use to defeat\n and destroy the many perils that might come in your way.")
        print()
        laundry = input("The weapons available in this room are a sword, an invisability cape, or both?\n You could just simply leave. (s,c,sc,leave) ")
        if laundry == 's':
                your_weapons.append("sword")
        direc4 = input("Where would you like to go? You can go either back, north-left, left, or south-left. (b,nl,l,sl) ")
        if direc4 == 'b':
                living_room() 
        elif direc4 == 'nl':
                bathroom_1()
        elif direc4 == 'l':
                kitchen()
        elif direc4 == 'sl':
                storage_1()
        elif laundry == 'c':
                your_weapons.append("invisability cape")
        direc4 = input("Where would you like to go? You can go either back, north-left, left, or south-left. (b,nl,l,sl) ")
        if direc4 == 'b':
                living_room() 
        elif direc4 == 'nl':
                 bathroom_1()
        elif direc4 == 'l':
                kitchen()
        elif direc4 == 'sl':
                storage_1()
        elif laundry == 'sc':
                your_weapons.append("sword")
                your_weapons.append("invisability cape")
                direc4 = input("Where would you like to go? You can go either back, north-left, left, or south-left. (b,nl,l,sl) ")
                if direc4 == 'b':
                        living_room() 
                elif direc4 == 'nl':
                        bathroom_1()
                elif direc4 == 'l':
                        kitchen()
                elif direc4 == 'sl':
                        storage_1()
        elif laundry == 'leave':
                direc4 = input("Your going to leave without any weapons? Have fun diying then I guess...\n Where would you like to go? You can go either back, north-left, left, or south-left. (b,nl,l,sl) ")
                if direc4 == 'b':
                        living_room() 
                elif direc4 == 'nl':
                        bathroom_1()
                elif direc4 == 'l':
                        kitchen()
                elif direc4 == 'sl':
                        storage_1()
        else:
                exit()
        
def storage_1():
        print("\t Honestly, there isn’t really much to say about this room than what it’s really used for. STORAGE!....\n BUUUTTT there are special equipment inside that might help you in case you get attacked\n by one of the monsters in this house.")
        print()
        storage_1 = input("The weapons availalbe in this room are a sheild, and a blow horn.\n You can pick up both or just one, your choice.\n You can also just simply leave if you like. (sh,b,shb,leave) ")
        if storage_1 == 'sh':
                your_weapons.append("sheild")
                direc3 = input("Where would you like to go? forwards, right, or upstairs onto the second level? (f,r,u) ")
                if direc3 == 'f':
                        kitchen()
                elif direc3 == 'r':
                        laundry()
                elif direc3 == 'u':
                        bathroom_2()
        elif storage_1 == 'b':
                your_weapons.append("blow horn")
                direc3 = input("Where would you like to go? forwards, right, or upstairs onto the second level? (f,r,u) ")
                if direc3 == 'f':
                        kitchen()
                elif direc3 == 'r':
                        laundry()
                elif direc3 == 'u':
                        bathroom_2()
        elif storage_1 == 'shb':
                your_weapons.append("sheild")
                your_weapons.append("blow horn")
                direc3 = input("Where would you like to go? forwards, right, or upstairs onto the second level? (f,r,u) ")
                if direc3 == 'f':
                        kitchen()
                elif direc3 == 'r':
                        laundry()
                elif direc3 == 'u':
                        bathroom_2()
        elif storage_1 == 'leave':
                direc3 = input("Well that sucks, you should've gotten some weapons.\n Where would you like to go? forwards, right, or upstairs onto the second level? (f,r,u) ")
                if direc3 == 'f':
                        kitchen()
                elif direc3 == 'r':
                        laundry()
                elif direc3 == 'u':
                        bathroom_2()
        else:
                exit()
        
def storage_2():
        print("\t Honestly, there isn’t really much to say about this room than what it’s really used for. STORAGE!....\n BUUUTTT there are special equipment inside that might help you in case you get attacked\n by one of the monsters in this house.")
        print()
        storage_2 = input("The weapons availalbe in this room are a sheild, and a blow horn.\n You can pick up both or just one, your choice.\n You can also just simply leave if you like. (sh,b,shb,leave) ")
        if storage_2 == 'sh':
                your_weapons.append("sheild")
        direc6 = input("Where would you like to go? south, or east? (s,e) ")
        if direc6 == 's':
                dining_room()
        elif direc6 == 'e':
                bathroom_1()
        elif storage_2 == 'b':
                your_weapons.append("blow horn")
        direc6 = input("Where would you like to go? south, or east? (s,e) ")
        if direc6 == 's':
                dining_room()
        elif direc6 == 'e':
                bathroom_1()
        elif storage_2 == 'shb':
                your_weapons.append("sheild")
                your_weapons.append("blow horn")
        direc6 = input("Where would you like to go? south, or east? (s,e) ")
        if direc6 == 's':
                dining_room()
        elif direc6 == 'e':
                bathroom_1()
        elif storage_2 == 'leave':
                direc6 = input("Well that sucks, you should've gotten some weapons.\n Where would you like to go? south, or east? (s,e) ")
                if direc6 == 's':
                        dining_room()
                elif direc6 == 'e':
                        bathroom_1()
        else:
                exit()
        
def parents_room():
        print("\t A very antique master bedroom with high class furnishings from very expensive wood found in the forests\n of the northern Canadian Shield. Everything was neat and tidy before the attack, however you can tell\n that it’s been haunted by both parents because from time to time some of the items inside the room with move from place to place!\n Pretty creepy huh!!!")
        print()
        print("Parent ghosts…The most annoying and deadly from them all! Both parents only go by their well known but very strong power, and that is to throw gigantic fire balls! Fuming in huge flames, the fire balls are half fire, and half molten rock!!!\n If you've already been in the laundry room, storage room, or bathroom you would've found some weapons in order to defeat these ghosts.\n You could use the sword, invisibility cape, shield, blow horn, or soap.")
        male_ghost()
        female_ghost()
        parent = input ("Choose a weapon {0}[Sword(s), Invisibility cape(c), Shield(sh), Blow horn(b), Soap(so)]​.".format(your_weapons))
        if parent == 's':
                print("A sword isn't going to help you when your going against gigantic fire balls.")
                exit()
        elif parent =='c':
                print("You can be invisable but the heat of the fire ball is too strong and csn still burn you up")
                exit()
        elif parent == 'sh':
                direc11 = input("You've defeated the two parent ghosts!\n Which way do you want to go now? Do you want to go west, north-west or south-west? (w,nw,sw) ")
                if direc11 == 'w':
                        bathroom_2()
                elif direc11 == 'nw':
                        bathroom_3()
                elif direc11 == 'ws':
                        twins_room()
        elif parent == 'b':
                print("Blow horns! It's just going to make them even more upset!")
                exit()
        elif parent == 'so':
                print("Soap? Lollllll thats so funny")
                exit()
        else:
                print("Game Over! You died!")
                exit()

def twins_room():
        print("\t The twin’s that used to sleep here were a crazy yet fun bunch. The oldest twin is a girl and she was 2 minutes earlier than her twin brother.\n Also, surprisingly enough that was the exact same time difference between both twins when they died! Coincidence?\n Any who, their room is compiled with a bunkbed, two desks, a play area, and two full length closets for each one.\n But of course to know which was who’s the items were colour coded as blue for the brother and red for the sister.")
        print()
        print("The evil twin ghosts are no ordinary pair of twins.\n They are way more deadly than you think. Trying to outrun them will never work since they are both telepathic thus making is almost impossible for you to make it through! What will you do?\n If you've already been in the laundry room, storage room, or bathroom you would've found some weapons in order to defeat these ghosts.\n You could use the sword, invisibility cape, shield, blow horn, or soap.")
        male_ghost()
        female_ghost()
        twins = input ("Choose a weapon {0}[Sword(s), Invisibility cape(c), Shield(sh), Blow horn(b), Soap(so)]​.".format(your_weapons))
        if twins == 's':
                print("A sword isn't going to help you when your going against ghosts.")
                exit()
        elif twins =='c':
                direc12 = input("You've defeated the evil twin ghosts!\n Which way do you want to go now? Do you want to go north or do you wanna go downstairs? (n,d) ")
                if direc12 == 'n':
                        storage()
                elif direc12 == 'd':
                        bathroom_2()
        elif twins == 'sh':
                print("The ghosts are gonna go through your sheild and attack you!")
                exit()
        elif twins == 'b':
                print("Blow horns! Really?")
                exit()
        elif twins == 'so':
                print("Soap? i dont't think so....")
                exit()
        else:
                print("Game Over! You died!")
                exit()
        
def brothers_room():
        print("\t The older brother’s room is a crazy mess! Just like every other teenager’s bedroom, it looks like a never ending maze of clothes, books, games, and other things!\n He did however had his bed done right before he was reportedly shot at the back of his head. No wonder there’s blood stains all over his white bedsheet.\n You can try going into his room but the chances of you leaving due to how messy the floor is will be very high. Good Luck!")
        print()
        print("The evil brother ghost is just like any other teenaged ghost. He tends to give a lot of attitude and will always get what he demands,\n Although, one of his weakest points is his huge collection of PumkiMon Cards. If you dare try and destroy them, He will disappear forever!\n If you've already been in the laundry room, storage room, or bathroom you would've found some weapons in order to defeat this ghost.\n You could use the sword, invisibility cape, shield, blow horn, or soap.")
        male_ghost()
        bro = input ("Choose a weapon {0} [Sword(s), Invisibility cape(c), Shield(sh), Blow horn(b), Soap(so)]​.".format(your_weapons))
        if bro == 's':
               direc10 = input("Yeah! You defeated the brother ghost!\n Which way do you want to go now? Do you want to go downstairs, or right? (d,r)")
        if direc10 == 'd':
                storage_1()
        elif direc10 == 'r':
                bathroom_3()
        elif bro == 'c':
                print("You will be invisable but it really won't help you. ")
                exit()
        elif bro == 'sh':
                print("A sheild will protect you but it won't let you destroy the most valuable collection of PumkiMon Cards.")
                exit()
        elif bro == 'b':
                print("The brother ghost really loves music...He's a teenager after all.")
                exit()
        elif bro == 'so':
                print("Soap? To destroy cards? I don't think so.")
                exit()
        else:
                print("Game Over! You died!")
                exit()
        
def main_room():
        print("\t Welcome to the main room!\n There really isn't much to do here besides leaving the haunted house or acctually going in.\n So are you up for the challenge or no?")
        direc = input("You have a choice as to where you would like to go. You can go either left, right, or up. Which way would you like to go? (l,r,u) ")
        if direc13 =='l':
                dining_room()
        elif direc13 == 'r':
                living_room()
        elif direc13 == 'u':
                storage_1()
        else:
                print("Uh oh! GAME OVER!!!")
                exit()
def female_ghost():
        print("                ¶¶¶¶¶¶¶    ")
        print("             ¶¶¶1111111¶¶¶ ")
        print("           ¶¶1111111111111¶¶  ")
        print("         ¶11111111111111111¶  ")
        print("      ¶1111¶¶11111¶¶¶¶1111¶11¶  ")
        print("    ¶11¶111¶¶__¶111¶___¶¶1111¶1¶  ")
        print("   ¶11¶111¶____¶¶111¶¶¶__¶111¶11¶  ")
        print("   ¶11¶11¶_______¶¶¶¶¶____¶11¶11¶   ")
        print("  ¶¶11¶111¶_________________¶111¶11¶¶ ")
        print(" ¶1111¶11¶___________________¶11¶1111¶ ")
        print(" ¶¶¶1¶1¶_____________________¶1¶1¶¶¶ ")
        print("   ¶111¶__¶¶¶___________¶¶¶__¶111¶  ")
        print("  ¶11¶1¶_¶___¶_________¶___¶_¶1¶11¶ ")
        print("  ¶1¶¶1¶__¶¶¶___________¶¶¶__¶1¶¶1¶  ")
        print("  ¶11¶1¶_¶_¶¶¶_________¶¶¶_¶_¶1¶11¶  ")
        print("  ¶11¶1¶_¶¶¶¶¶_________¶¶¶¶¶_¶1¶11¶  ")
        print("   ¶111¶¶_¶¶¶__¶__¶__¶__¶¶¶_¶¶¶11¶  ")
        print("    ¶111¶_______¶¶_¶¶_______¶111¶  ")
        print("     ¶¶¶¶¶_________________¶¶¶¶¶   ")
        print("          ¶_____¶¶¶¶¶_____¶      ")
        print("           ¶___¶¶¶¶¶¶¶___¶     ")
        print("            ¶¶_________¶¶     ")
        print("              ¶¶¶¶¶¶¶¶¶     ")
        print("          ¶¶¶__¶___¶__¶¶¶    ")
        print("          ¶¶_____¶¶¶_____¶¶  ")
        print("         ¶1¶_____________¶1¶  ")
        print("         ¶11¶___________¶11¶   ")
        print("         ¶111¶¶_______¶¶111¶   ")
        print("         ¶11111¶¶¶¶¶¶¶11111¶  ")
        print("         ¶11¶11111111111¶11¶  ")
        print("        ¶11¶1111111111111¶11¶  ")
        print("        ¶11¶1111111111111¶11¶  ")
        print("       ¶111¶1111111111111¶111¶   ")
        print("       ¶111¶1111111111111¶111¶    ")
        print("      ¶111¶111111111111111¶111¶   ")
        print("    ¶¶1111¶111111111111111¶1111¶¶  ")
        print("   ¶¶_¶11¶11111111111111111¶11¶_¶¶  ")
        print("  ¶1¶__¶1¶11111111111111111¶1¶__¶1¶ ")
        print(" ¶111¶¶¶¶1111111111111111111¶¶¶¶111¶  ")
        print(" ¶1111111¶1111111111111111111¶1111111¶  ")
        print(" ¶111111¶111111111111111111111¶111111¶  ")
        print(" ¶11111¶11111111111111111111111¶11111¶  ")
        print("  ¶111111111111111111111111111111111¶   ")
        print("   ¶1111111111111111111111111111111¶   ")
        print("    ¶¶111111111111111111111111111¶¶  ")


def male_ghost():
        print("            ▒▒▒▒▒▒▒▒▒      ")
        print("        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ")
        print("       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ")
        print("      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ")
        print("     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ")
        print("     ▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒   ")
        print("   ▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒   ")
        print("   ▒▒▒▒██████▒▒▒▒▒▒▒▒▒██████▒▒▒▒  ")
        print("   ▒▒▒███▐▀███▒▒▒▒▒▒▒███▀▌███▒▒▒  ")
        print("   ▒▒▒██▄▐▌▄███▒▒▒▒▒███▄▐▌▄██▒▒▒  ")
        print("   ▒▒▒▒██▌███▒▒▒█▒█▒▒▒███▐██▒▒▒▒  ")
        print("  ▒▒▒▒▒▒███▒▒▒▒██▒██▒▒▒▒███▒▒▒▒▒▒  ")
        print(" ▒▒▒▒▒▒▒▒█▒▒▒▒██▒▒▒██▒▒▒▒█▒▒▒▒▒▒▒▒ ")
        print(" ▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒ ")
        print(" ▒▒▒▒█▒▒█▒▒▒▒██▒▒▒▒▒██▒▒▒▒█▒▒█▒▒▒▒  ")
        print("  ▒▒▒█▒▒█▒▒▒▒█▒██▒██▒█▒▒▒▒█▒▒█▒▒▒  ")
        print("   ▒█▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒█▒   ")
        print("    ▒▒█▒▒▒▐███████████▌▒▒▒█▒▒     ")
        print("       ▒▒▒▐█▀██▀███▀██▀█▌▒▒▒     ")
        print("       ▒▒▒▒█▐██▐███▌██▌█▒▒▒▒    ")
        print("       ▒▒▒▒▒▐▒▒▐▒▒▒▌▒▒▌▒▒▒▒▒    ")
        print("        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      ")
        print("        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      ")
        print("         ▒▒█▒█▒▒▒█▒▒▒█▒█▒▒      ")
        print("         ▒██▒█▒▒▒█▒▒▒█▒██▒      ")
        print("              ▒▒███▒▒         ")
        print("              ▒█████▒          ")


def dust_bunny():
        print("                   ¶                ¶ ")
        print("                  ¶¶                ¶¶ ")
        print("                ¶¶¶                  ¶¶¶ ")
        print("              ¶¶¶¶                    ¶¶¶¶  ")
        print("             ¶¶¶¶¶                    ¶¶¶¶¶  ")
        print("            ¶¶¶¶¶                      ¶¶¶¶¶ ")
        print("           ¶¶¶¶¶¶                      ¶¶¶¶¶¶  ")
        print("           ¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶  ")
        print("           ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ")
        print("           ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ")
        print("            ¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶    ¶¶¶¶¶¶¶¶  ")
        print("   ¶        ¶¶¶¶¶¶¶      ¶¶¶¶      ¶¶¶¶¶¶¶   ")
        print("   ¶       ¶¶¶¶¶¶¶¶   O  ¶¶¶¶  O   ¶¶¶¶¶¶¶   ")
        print("  ¶¶¶      ¶¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶    ¶¶¶¶¶¶¶¶¶  ")
        print("  ¶¶¶     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ")
        print(" ¶¶¶¶¶    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶   ")
        print(" ¶¶¶¶¶    ¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶  ")
        print("   ¶¶     ¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶  ")
        print("   ¶¶      ¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶   ")
        print("    ¶¶      ¶¶________¶¶¶¶¶¶¶¶¶¶_______¶¶    ")
        print("    ¶¶       ¶¶¶_______________________¶    ")
        print("     ¶¶        ¶¶____¶¶¶¶¶¶¶¶¶¶¶______¶     ")
        print("      ¶¶        ¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶__¶     ")
        print("       ¶¶          ¶¶¶_____¶¶¶¶¶¶¶¶¶¶   ")
        print("        ¶¶           ¶¶¶¶¶__¶¶¶¶¶¶¶¶¶   ")
        print("                             ¶¶¶¶¶¶¶¶¶¶   ")
        print("                              ¶¶¶¶¶¶¶¶¶   ")
        print("                               ¶¶¶¶¶¶¶    ")

def killer_clown():
        print("                      ..:::::::::::::.. ")
        print("                .:::::''              ``:::. ")
        print("              .:;'                        `::. ")
        print("           ..::'                            `::. ")
        print("          ::'                                  ::.:' ")
        print("      `::.::                                    ::. ")
        print("    .::::::::'                                `:.:::.    .:':' ")
        print(":::::::::::::.          .:.                .:. ` :::::::::'::: ")
        print(":::.::::::::::::'       :::                :::    :::::::::':::' ")
        print("..::::::::::::'          ' `                ' `   .::::::' :::' ")
        print("::::::::::::'  `:.   .:::::::.          .:::::::.:: .:' :'.::' ")
        print("::::::::::::    `::.::'     `::.      .::'     `::.::':'.:::' ")
        print("::::::::::::      .::'        `:;  . .::'        `:;:'.::''  ")
        print(":::::::::::'.     ::'    .    .:: :  ::'    .    .:::::'' ")
        print(":`::::::::::::.:  `::.  :O: .::;' :  `::.  :O: .::;'::' ")
        print("   `::::::`::`:.    `:::::::::'   :.   `:::::::::':''' ")
        print("       `````:`::.     , .         `:.        , . `::. ")
        print("            :: `::.   :::      ..::::::::..  :::  `:: ")
        print("      .::::'::. `::.  `:'     :::::::::::::; `:'   :;  ")
        print("            ::'    ::.   .::'  ``:::::::;'' :.   .:' ")
        print("            `::    `::  ::'        ::       .::  :'  ")
        print("             ::.    :'.::::::.    :  :   .::::. .:::. ")
        print(":.           `::.     :::'  ``::::. .::::'' `::::' `::. ")
        print("`::.          `::.    `:::. ::.  `::::' .:: ::::;    `:: ")
        print(":.`:.          `::.     `::. `:::.    .::'  ::;'     .:;. ")
        print(" ::`::.          `::.     `::.  `::. .::' .:;':'     :;':. ")
        print("::':``:::::.       `::.     `::. `::::'  .:;':'     .;':': ")
        print(": .:`:::':`:::::.   `::.      `:::.   .::;'.:'  .::;'' ';: ")
        print("..::': :. ::::. `::::::`::..      `:::::'  .:':::'::.:: :': ")
        print(":' :'.:::. `:: :: ::. .::`::.   .     . .:;':' ::'`:: :::' ")
        print(": ::.:. `:  `::'  `:: ::'::`::::::::::::;' :: .:' .::: ;:' ")
        print("::.::.:::: .:: :.  `:':'  ::.:'`::. .::':.::' :: .::''::' ")
        print("`:::`::.`:.::' ::  .: ::  `::'  `:: :' .::' ::.:.::' :; ")
        print("   `::::::.`:. .:. :: `::.:: ::  `::. .:: ::.`:::':.:;' ")
        print("         `::::::::::...:::'  `::.:'`:.::'.:.:;' .:;' ")
        print("                    `::::::::::::::::::::'.::;:;' ")


## Beginning of my program

## Main Program
print("Welcome to the Haunted House of the Harris'!")
print()
enter = input("Do you have the guts to enter this horrifying, yet mysterious looking house? (y/n)")
if enter=='y':
        print("\nThe Harris' were a family of 5 whom used to live in this exact home 25 years ago\nIt all ended when the family died from an unknown suspect whom decided to enter the house and call fire to all members of the family...\nHowever since their death, there remains and belongings have been left inside their house. Rumor has it that their souls are still roaming around in readiness to haunt other visitors who come to the house...\nNo wonder it's haunted!")
elif enter=='n':
        print("What! You chickened out?")
        exit()

## Main room or entrance to game
print()
direc = input("You have a choice as to where you would like to go. You can go either left, right, or up. Which way would you like to go? (l,r,u) ")
if direc =='l':
        dining_room()
elif direc == 'r':
        living_room()
elif direc == 'u':
        storage_1()
else:
        print("Uh oh! GAME OVER!!!")
        exit()


        
