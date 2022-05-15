import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you =='w':
            return False
        elif you == 'g':
            return True 
    elif comp == 'w':
        if you =='g':
            return False
        elif you == 's':
            return True 
    elif comp == 'g':
        if you =='s':
            return False
        elif you == 'w':
            return True 
        
print("a Turn: Snake(s) Water(w) or Gun(g)?")
randNO = random.randint(1, 3)

print(randNo)
if randNO == 1:
    a = 's'
elif randNO ==2:
    a = 'w'
elif randNO ==3:
    a = 'g'


you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")

a = gameWin(comp, you)
print(f"You choose {comp}")
print(f"You choose {you}")

if randNO== None:
    print("The game is a Tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
    