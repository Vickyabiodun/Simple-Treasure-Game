<h2>Prerequisites</h2>
<p>Before you begin, make sure you have the following tools installed on your computer:</p>
<ul>
  <li>A text editor (such as Sublime Text or Atom)</li>
  <li>Python 3</li>
</ul>
<h2>Step 1: Create a new Python file</h2>
<p>Open your text editor and create a new file. Save the file as <code>ascii_art_game.py</code>.</p>
<h2>Step 2: Add the ASCII art</h2>
<p>The first thing we need to do is add the ASCII art to our file. Copy the following block of code and paste it into your file:</p>
<pre><code>
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
</code></pre>
<p>This block of code will print the ASCII art and a welcome message to the console when the game is run.</p>

<h2>Step 3: Add the first input and conditional statement</h2>
<p>Next, we will add the first input and conditional statement. This will allow the player to choose a direction and determine the next step in their journey.</p>
<p>Copy the following block of code and paste it into your file:</p>
<pre><code>first_que = input('where would you love to go, left or right?')

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
</code></pre>
<p>This block of code will prompt the player to choose a direction (left or right). If the player chooses left, they will be asked whether they want to swim or wait. If they choose swim, the game will end and they will have drowned. If they choose wait, they will be asked to choose a door (blue, red, or yellow). If they choose blue or red, the game will end and they will be burnt. If they choose yellow, they will win the game and find the treasure!</p>
<h2>Step 4: Test the game</h2>
<p>To test the game, open a terminal window and navigate to the directory where you saved the file. Then, run the following command:</p>
<pre><code>python ascii_art_game.py
</code></pre>
<p>The game should now be running, and you can follow the prompts to play through the adventure.</p>
<h2>Step 5: Customize the game</h2>
<p>You can customize the game by modifying the ASCII art, the prompts, and the outcome of the different choices. Have fun experimenting with different combinations and creating your own unique adventure!</p>
