import random
# snake water gun or rock paper scissors.
def gameWin (comp, you):
    # if two values are equal declare a tie
    if comp == you:
        return None
    # check for all possibility when coputer chose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    # check for all possibility when coputer chose w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    # check for all possibility when coputer chose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print ("comp turn turn: Snake(s) Water(w) or Gun(g) ?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
you = input ("your turn: Snake(s) Water(w) or Gun(g) ?")


a = gameWin (comp, you)

print (f"computer chose {comp}")
print (f"you chose {you}")
if a == None:
    print ("the game is a tie")
elif a:
    print ("you win!")
else:
    print ("you lose!")