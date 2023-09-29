**moday september 28th**


# CTE Work # 

<img width="1280" alt="Screenshot 2023-09-28 224312" src="https://github.com/FantasticMrCat42/2023-2024/assets/129550102/57b5529c-c0c5-4bd3-9b7d-57b2c3253ad2">

this week we worked on a veriety of metthods to create working feedback device for the CTE project. the CTE Project is a project for the Spring Branch school distric for an upcoming event. the information about the event can be found on there website here : https://www.springbranchisd.com/success

## Outline ##
Our plan is to use a pre-existing design for the input device created by one of the other groups working on this project. if we have the time we can work on creating our own iteration but we have limited time in class to complete the project. We will be using the makey makey a input device that can interface with the computer acting as keystrokes. to create the program I will be using scratch because the makey makey was natively suported in scratch which is garenteed to work on the crombook.

### Criteria ###
-  the device must be reprodicable so that it can be used at multiple point through out the event
-  the device and code must work with the school cromebook
-  the program will offer questions to the user and will record responses

### Creation Prosses ###
originaly when working in scratch i identified the issue of storing the data. if we wanted to seperate the data in a way that could be read easily by the user afterward we whould need a list or variabls. the isues with variables is that they can only be labled as one thing and while they could store multiple answer options it whould require a decoding prosses wich whould defeat the perpose. instead I decided to use a list. scratch is a limited block based coding language created by MIT to introduce children to the concept of coding and the basic components in a simple and intuitive way. this presented problems as the only was to store data was in a variable or in list. even with these limitations many programers have created impressive projects including a 3D FPS game as well as a 3D platformer. both utilize Raycasting an old techniche used in early 3D games like wol here are some truly impressive projects: [Here](https://turbowarp.org/463553665?hqpen&size=640x360&fps=60)

with the limitations of scratch I needed to find solutions to limitations such as a lack of arrays. my first attempt was to create a system that recorded each of your answers in a list that whould be read by the user. while this solution worked it was to problematic to be practical. my final solution used a loop that whould cicle through the list of questions by swaping the sprites apperence for the diferent questions. a second loop whould then record the users respons and store it in a list titled Answers. this made up the basis of the system for recording answers but I also needed to decode the answers from the list to do so I created a loop that whould devide the length of the list by five then search evry 5th answer then record its value in 3 variable that whould temporaraly hold the amount of red green and yellow responses. it whould then enter this into a second list with the labled data then it whould do the same for evary other question.

to find my scratch project you can visit this link: https://scratch.mit.edu/projects/900403964/
