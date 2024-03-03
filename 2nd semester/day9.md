# Space filling curves
  the first video disccuses space filling curves that act like fractals. a space filling curve can fill the entirty of a 2d area even as a infinantly thin line. this is only posible because the line is a fractal can continuesly fill the area. 

  the next video follows a path finding algorithm that is similer to those used in games wich is normaly A*. 
  <img width="399" alt="Screenshot 2024-03-03 153241" src="https://github.com/FantasticMrCat42/2023-2024/assets/129550102/33129c07-4613-4001-bdc8-5a323de1e780">
in the video on dark soels goes into more deapth with video game path finding algorithms but it left me with a question? how does the game decide what is considerd a point. in all the exaples there are clearly defined points and in a game like minecraft evrything is a grid so it makes sence but in a fully 3d game how does it decide that somthing is a point. if it just lays a predefined grid of points then eliminates the ones that colide with objects you whould have way to many points.

# drawing mazes
the first video uses stacks as a history of the visited poitns on the grid when constructing the maze. so once the algorith hits a dead end it will back track using the pop feature. then to construck the maze the program draws lines in between the paths. so it almost uses a path finding agorithm to find a ton of paths unitll it fiills the grid. then the maze is constructed around it.

# Mouse maze
flood fill algorithm was listed in the video as the most used as it can find a fast path to the objective while ignoring irelevent portions of the maze. the most interesting part of the video is probably the diferent ways used to cut time such as taking diagnal turns.
