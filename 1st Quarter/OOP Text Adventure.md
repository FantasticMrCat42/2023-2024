**moday september 18th**


# More About OOP # 

<img width="1795" alt="Screen Shot 2023-09-22 at 2 40 48 PM" src="https://github.com/FantasticMrCat42/2023-2024/assets/129550102/925fd7a1-903c-4643-a749-8c4ef89b8099">



this week i worked on a top down text adventure using OOP. I mainly focused on usinf the shapes library to create the visuals. I ussed classes for repeating charachters like enemys or chest as to include data like loot

to do this I aligned the player with a grid. to do this i set the players position to zero and only allowed the player to move by 50 so that I can easily align objects. if they have the same x and y position as a chest the player can  interact by pressing the E key. then the code randomizes a value wich it then pulls from a loot table list. this then is inserted into a list for the players inventory.

my plan is that the player will navigate a top down dungen but when they enter a new area the text will print in the console describing any details that the simple top down view wont show.
https://replit.com/@HensonLiga/EmptyFrightenedLicenses




```
from shapes import Paper, Rectangle, Oval, Triangle
import os
import random

paper = Paper()
rect1 = Rectangle()
PlayerBody = Rectangle()
enemyBody = Rectangle()

rect1PosX = 250
rect1PosY = 250
rectClear = Rectangle()
rectClear.set_color("white")
rectClear.set_x(0)
rectClear.set_y(0)
rectClear.set_height(1000)
rectClear.set_width(1000)

PlayerBody.set_color("#FADFB7")
PlayerBody.set_x(250)
PlayerBody.set_y(250)
PlayerBody.set_height(50)
PlayerBody.set_width(50)

def DrawPlayer():
  
  PlayerBody.draw()
  

chestX = 300
chestY = 300
def DrawLoot():
  enemyBody.set_color("#5A4743")
  enemyBody.set_x(chestX)
  enemyBody.set_y(chestY)
  enemyBody.set_height(50)
  enemyBody.set_width(50)
  enemyBody.draw()

itemlist = ['bow', 'arrows', '10 gold']
diologe = ["room 1", "Room 2", "Room3", "Press E to open chest", "chest opened"]
inventory = []
x = 0
while (True):
  print(diologe[x])
  print(inventory)
  inputVal = input()
  rectClear.draw()
  
  if (inputVal ==  "a"):
    rect1PosX = rect1PosX - 50
    rect1.set_x(rect1PosX)
  elif (inputVal == "d"):
    rect1PosX = rect1PosX + 50
    rect1.set_x(rect1PosX)
  elif (inputVal == "w"):
    rect1PosY = rect1PosY - 50
    rect1.set_y(rect1PosY)
  elif (inputVal == "s"):
    rect1PosY = rect1PosY + 50
    rect1.set_y(rect1PosY)

  if (rect1PosX == chestX and rect1PosY == chestY):
    x = 3
    if (inputVal == "e"):
      x = 4
      item = random.randrange(0,3)
      inventory.append(itemlist[item])
      
      
  
    
  rect1.draw()
  DrawLoot()
  x = x
  os.system('clear')
  
  



paper.display()

```
