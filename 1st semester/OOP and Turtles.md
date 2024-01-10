**OOP and Turtles**


# Working with Turtles # 

this week I Worked on learning Object oriented programing as well as how to use the turtle python library. I have used OOP before when working with Unity because basicly evrything in unity uses OOP. I mainly focused on using the turtle library and created a crude depiction of a man with a handle bar mustache as depicted bellow.

![Screenshot 2023-09-23 164911](https://github.com/FantasticMrCat42/2023-2024/assets/129550102/e314f6f5-7190-4db1-9c63-1d619225c312)

I also expored using the .clone method to create 2 different turtles but I did not have the time to make the turtles move at the same time.

this is my code to create the mustash. I import the turtle library to get the turtle functions then i define a variable as a turtle. i used loops to create the spiral affect with i decaying variable to make the loops tighter as it continued. 


 ```
import turtle


t1 = turtle.Turtle()
t2 = turtle.Turtle()
t2.right(180)
for i in range(34):
  t1.forward(5)
  t1.left(i)

for i in range(34):
  t2.forward(5)
  t2.right(i)

t1.penup()
t1.setpos(10,70)
t2.penup()
t2.setpos(-10,70)
 ```

before creating the mustash i was experimenting with the Clone command in an atempt to create a tree fractel pattern simmiler to the one bellow. the issue i ran into was trying to code the turtle to clone at each jusction then pick a diferent direction. because i had to define each turtle with a variable i couldent make the fractal easly. unfortunatly i saw i was running out of time so i created a mustash using the clone function.
![maxresdefault](https://github.com/FantasticMrCat42/2023-2024/assets/129550102/389ee55c-a60f-42eb-a76b-c6b6117fe3c3)


