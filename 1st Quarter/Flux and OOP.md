1. all the cards in the game of fluxx could be considerd under the Superclass of card with subclasses to seperate them into Keepers, Goals, Actions

2. each individual card could be considerd an instance

3. diferent atibutes of the card including its effect could be considers Attribute: a named piece of data stored within an object

4. Method: a function which performs a task on an object or tells the object what to do - this couold be when a player uses an action card because it affects other cards

5. Subclass: inherits the properties of another class and adds some specialised methods of its own - each individual card type whould be a subclass of the of the superclass of all cards

6. the player could also be considerd an object holding the difrent cards wich whould be Aggregation

7.  Extend: a class that uses the functionality of an existing class, but also adds to or overwrites some of it - specific cards under there class of goal could extend this to be specificly "two keepers that add to the number 2" so specific rules

8.  Constructor: a special method to tell Python how to create an object of this class: in Python, the constructor method is always called __init__ with a double underscore on each side of ‘init' - the overarching goal card class whould have a constructer to build goal cards because all goal cards have similer functions with minor variations
