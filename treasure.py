
"""This is an ascii art"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

"""The first input and conditional statement"""

first_que = input('where would you love to go, left or right?')

if first_que.lower() == 'right':
    print('Game Over')
elif first_que.lower() == 'left':
    second_que = input('would you love to swim or wait?')
    print(second_que)
    if second_que.lower() == 'swim':
        print('Game Over, you drowned')
    elif second_que.lower() == 'wait':
        third_que = input('which door would you love to follow, blue, red or yellow?')

        print(third_que)
        if third_que.lower() == 'blue':
            print('Game Over, you got burnt')
        elif third_que.lower() == 'red':
            print('Game Over, you got burnt')
        elif third_que.lower() == 'yellow':
            print('Congratulation, you made it. You won!!!')
        else:
            print('Game Over, you lost')
    else:
         print('Game Over, you drowned')   
else:
    print('Game Over')


