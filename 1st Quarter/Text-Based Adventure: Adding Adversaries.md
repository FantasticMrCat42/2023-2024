# Text-Based Adventure: Adding Adversaries #

this week I worked on expanding my knolage of OOP and experemented with using object oriented coding in the context of a text based adventure game. this week I also worked on finnishing the document to create a computer science national honor society. 

# my work with OOP #
first I followed the slides and created a method to move between romes by typing the cordinal direction. this used a dictinary to list the conected rooms and whould take the user input and send the player to the coresponding room in the dictionary defonition. the code used to link and move between rooms is bellow.

```
def link_room(self, room_to_link, direction):
      self.linked_rooms[direction] = room_to_link
    
  def move(self, direction):
      if direction in self.linked_rooms:
        return self.linked_rooms[direction]
      else:
        print("cant go that way")
        return self
```

after this I took a quiz in replit covering the vocabulary from the preveos OOP lessons.
<img width="1280" alt="Screenshot 2023-10-26 154442" src="https://github.com/FantasticMrCat42/2023-2024/assets/129550102/13684f10-64fa-4c52-9ed3-3b7cb121af48">

## adding Adversaries ##
I worked throught the slides and learned about sub and super classes.

my code is linked [here](https://replit.com/@HensonLiga/txt-Adventurepy)

I took the second quiz over OOP concepts.

<img width="929" alt="Screenshot 2023-11-23 180831" src="https://github.com/FantasticMrCat42/2023-2024/assets/129550102/555b0ced-aeda-40a8-af11-ce4a3e647fdc">
