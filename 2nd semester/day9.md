# Space filling curves
  the first video disccuses space filling curves that act like fractals. a space filling curve can fill the entirty of a 2d area even as a infinantly thin line. this is only posible because the line is a fractal can continuesly fill the area. 

  the next video follows a path finding algorithm that is similer to those used in games wich is normaly A*. 
  
  <img width="399" alt="Screenshot 2024-03-03 153241" src="https://github.com/FantasticMrCat42/2023-2024/assets/129550102/33129c07-4613-4001-bdc8-5a323de1e780">
  
in the video on dark soels goes into more deapth with video game path finding algorithms but it left me with a question? how does the game decide what is considerd a point. in all the exaples there are clearly defined points and in a game like minecraft evrything is a grid so it makes sence but in a fully 3d game how does it decide that somthing is a point. if it just lays a predefined grid of points then eliminates the ones that colide with objects you whould have way to many points.

# drawing mazes
the first video uses stacks as a history of the visited poitns on the grid when constructing the maze. so once the algorith hits a dead end it will back track using the pop feature. then to construck the maze the program draws lines in between the paths. so it almost uses a path finding agorithm to find a ton of paths unitll it fiills the grid. then the maze is constructed around it.

# Mouse maze
flood fill algorithm was listed in the video as the most used as it can find a fast path to the objective while ignoring irelevent portions of the maze. the most interesting part of the video is probably the diferent ways used to cut time such as taking diagnal turns.

the final video covers a maze that uses somthing akin to gas particles to solve the maze. its just places a flood of particles in and the first one to randomly reach the end has found a path. this remindes me of the sorting algorithm bogo sort which is "sort the elements of an array by randomly generating different permutations of an array and then checking whether it is sorted or not". the bogo sort algorithm is random and is far worse than the one using particles from the video but i just rememberd it when he called his the dumb way of finding the path

Come up with 10 potential ideas for your semester project, related to topics, and/or concepts we've worked on so far this semester.

For each:
 - briefly describe the idea
 - state which topics/concepts it relates to

# Part 0a - Idea Generation
- mazes genorator [this whould be just a simple maze generator like the ones we saw in class. we never realy got to make are own and i think it whould be fun]
- a pathfinding bot [same as the maze I think that making a pathfinding bot whould be usfull. partly because it could be reused in games.]
- make a sim game [this whould be like a sim or maybe somthing like CIV but im not sure I could make somthing good in the time we have (or with more time, because I kinda suck at making games)]
- make a zombie simulation [make a sort of zombie survival simualtion with a carachter and the dificulty setings allowing you to addjust the model]
- terain genaration [a simple terain generator using noise whould be fun. I did this last year with my planet generator but I think I could add more this time. also i could combine this with the path finding algorithm to make a simulaiton of some sort]
- light simulation with ray casting [thsi is simmiler to my scratch game that I made a while back. it used ray casting to create the 3D effect simmiler to games like Woolfinstine 3D from john carmack  ]
- phyisics simulation [this could be like a water simulation or just a basic gravity simulation]
- POOL SIM / BILULARDS [this whould be like the physics simulation but I could also see if I could do some website hosting and make it like the game pigen game because that only works on apple and i want a solution, I could use a website or I could have the result of a move be encoded then encripted so that you could send that in text form to denote what happend]
- make that plant simulation (probably too hard (unless its in python(i dont like java)))[the plant simulation was somthing I planned on doing earlier but whould most likely be too hard unless I used python. I could do it in java but no mater what the project is going to take more than the class time I have and I will eat a jar of mayonaise before I code java in my free time]
- a cool pinball simulator (basicly the pool simulato but it whould be harder) [this is like the pool game but I whould probably extend it into the 3rd dimension. so basicly a physics sim but I dont need to do anything other than impacts and colisions]

<img width="338" alt="image" src="https://github.com/FantasticMrCat42/2023-2024/assets/129550102/df8f9ab4-5c6a-46d1-9e2b-03ad4d45a311">


Choose 2 of your ideas.

For each of these 2:
- Sketch out the idea
- Find 2 resources that could help you with this idea
- -- For each of these resources:
- -- -- provide the title and URL of the specific resource
- -- -- tell me why you think it may be helpful.

# PROJECT: Part 0b - Sketches / Resources
{Idea #1 : further work on my AIVA project}
I plan on connecting my connecting my AI hand detection and upgrading my AI vison model to better intigrate into eachother for the project the following are some changes I need to make:
-  I could add text to speach AI for navigating the menues
-  I could add the open AI whisper model for voice recogniton
-  I need to update my deapth recognition AI with the new Moneculare deapth estimation model

Resources:
the first scources is the [depth anything model](https://github.com/LiheYoung/Depth-Anything)
- I will use this to update my curent deapth model to hopfully be more accurate and add metric deapth estimation instead of relitive estemation. this will be used for the obstical recognition to warn the user of obsticals. this scource has some example code as well as a explinaiton of the model.
  
the second rescource is the [whisper model](https://github.com/openai/whisper). 
- I think this will be usfull for audio transcription of the users voice. this github repo includes some example code so I can addapt that for my project

{Idea #2 : pool simulation}
for this project I could work on crating a pysics simultaion of the pool balls and the pool cue. the player could interact with the simulation and compeate with another player.
- I whould most likely base the gameplay mecaniks off of the game from game pigion.
- the balls whould all be objects with force vectores that act on eachother.
- I the balls whould also have a friction force to slow them down
  sudo sudo code:
  - a startup protion that spawns the balls in the correct location according to an array
  - a loop that updates evry players turn
    - within the loop is another loop that whould calculate the effects of the players moves including the balls and the drag and collisions
     - a score check function to update the score
   
  Resources:
  my first resource is a video on [simulating pysics in python](https://www.youtube.com/watch?v=5j0uU3aJxJM)
  - I would use this to make the base collision physics in my game. so that ball collisons and the players moves whould act like a real simulation
  my second scource is on [how to use pygame](https://www.youtube.com/watch?v=y9VG3Pztok8)
- I need this scource because alot of this game will require the pygame package most likely
