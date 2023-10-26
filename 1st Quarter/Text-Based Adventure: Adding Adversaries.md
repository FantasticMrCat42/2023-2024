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

