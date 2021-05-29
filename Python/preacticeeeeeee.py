def dining():
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

print()
direc = input("You have a choice as to where you would like to go. You can go either left, right, or up. Which way would you like to go? (l,r,u) ")
if direc =='l':
        dining_room(dining)
elif direc == 'r':
        living_room()
elif direc == 'u':
        storage()
else:
        print("Uh oh! GAME OVER!!!")
        exit()
        
