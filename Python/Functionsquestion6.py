def wrong_answer():
    print("    \|/ _____ \|/")
    print("     @~/  ,. \~@ ")
    print("    /_( \___/ )_\  ")
    print("       \___U_/      ")

def right_answer():
    print("  YAY!  ____     ")
    print("     @ /_**_\ @ ")
    print("    /_( \##/ )_\ ")
    print("       \____/    ")

q1 = int(input("What's 2 plus 2?"))
if q1 == '4':
        print(right_answer())
else:
        print(wrong_answer())
        
q2 = int(input("What's 25 times 4?"))
if q2 == '100':
        print(right_answer())
else:
        print(wrong_answer())
        
q3 = int(input("What's 28 divided by 4?"))
if q3 == '7':
        print(right_answer())
else:
        print(wrong_answer())

    
