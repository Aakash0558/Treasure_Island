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

Player = input("Player, please enter your name: ")

decision_directions = input("You start at crossroads, which way do you want to head first, left or right? ").lower()

if (decision_directions == "left"):
  print("As you traverse the path on your left, you have reached a river. Now you can relax for sometime here!")
  decision_ToSwim = input(Player + ", do you choose to swim or do you choose to wait? ").lower()
  if (decision_ToSwim == "wait"):
    print("Choosing to wait pays off. Three giant doors with different colors appear infront of you!!!")
    decision_doors = input(Player + ", what colored door do you wish to enter? ").lower()
    if (decision_doors == "yellow"):
      print("YOU HAVE FOUND THE TREASURE CHEST!!!! YOU HAVE WON THE GAME, CONGRATULATIONS" + " " +  Player.upper() + "!!!!")
    elif (decision_doors == "red"):
      print("The door closes as soon as you enter. The temperature in the room is rising, now the room is slowly getting engulfed in flames. The door isn't opening. You caught the fire and now you are burned to crisp. You are dead, GAMEOVER!!")
    elif (decision_doors == "blue"):
      print("As soon as you open the door, beasts come out chasing you. You run as fast as you can to escape them but it's all in vain. You are eaten alive by the beasts of the blue door. You are dead, GAMEOVER!!")
    else:
      print("You have died mysteriously, GAMEOVER!!")
  else:
    print("You tried to swim over the river, but creatures of the sea have attacked you, you are fatally injured and due to the water you are losing consciousnes. You have died, GAMEOVER!!")
else:
  print("You are traversing the path on your right. As you keep going on, you suddenly fall into a invisible hole and have died. GAMEOVER!!")
