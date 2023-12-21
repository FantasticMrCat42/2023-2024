## Project Write-Up ##
# Summary #
this project focused on creating a intuative but somewhat adavanced user interface for generating images with Stable diffusion. in the end I feal I made valuable progress twords that goal and learned alot I plan on using when I make a second implimentation. the main issues I faced was the diffusers python library by hugginh face. while it was easy and had lots of documentation I still ran into several issues when trying to run the models entirly localy.

# Skills #
- utilizing new python librarys
- Object oreantated programing
- Tkinter
- custom Tkinter
  
![Screenshot 2023-12-19 171516](https://github.com/FantasticMrCat42/2023-2024/assets/129550102/ac3fc111-dd4d-4ed7-824a-c6327fd83e3f)

# Overview #

to create the GUI I am using the custom Tkinter library instead of the basic Tkinter library. the custom tkinter library is almost the exact same as Tkinter but it inludes a more adjustable UI including dark mode. I started the project by trying to learn the Diffusers library. the main issues I faced with this project was getting mutiple inputs to sync in the GUI. to avoid this issue I just limited the user interface to single inputs and disabled the sliders. i also revisitid the PIL library to display and adjust images to fit the interface. I plan on expanding it further but the code is rushed and should honestly be rewriten. In the prosses of making the GUI I used several Tkinter widgets including the text entrys for the prompt and negative prompt. I inluded sliders for adjusting settings but Never ended up using them because I needed to sync them to the input boxes used for the same settings.

![Screenshot 2023-12-19 171534](https://github.com/FantasticMrCat42/2023-2024/assets/129550102/17d4dc1a-b5a4-4209-b851-bf74af522035)
## SKILLS EXIBITED ##
THREADING

i learned more about using threading in python. the implimentation kinda sucks and I am still trying to get better but it was quite literaly vital when creating this project because if you run the diffusion model and the UI at the same time it will freeze while genorating the image

![image](https://github.com/FantasticMrCat42/2023-2024/assets/129550102/1f3de57f-fe0a-4a3c-a206-a99eb93d5e79)

the .thread() method is also an example of object orentated coding because ive defined an object as t1 and am calling a method from the class.

USING OS LIBRARY AND GUIS USING TKINTER

i learned how to read the path of files in a folder. this was used in geting the file list for avalable models

![image](https://github.com/FantasticMrCat42/2023-2024/assets/129550102/d352ed89-d063-4ad9-a165-8fa72563b103)

this is another case of OOP as to display the model dropdown I am using tkinter which considers parts of the GUI like dropdowns as Objects


USING FUNCTIONS IN SEPERATE FILES

i set up my functions in separate files to make a more organized project. this ended up being counter productive becuse after I finished the image I needed to display the users inputs like seed which was genorated within the function. In the case of displaying the image via its path I had to make a workaround and in the future I will need to restructure my generation method

![image](https://github.com/FantasticMrCat42/2023-2024/assets/129550102/c44e2720-ef03-4fff-aa32-fd6c14c90ffe)

theres not much OOP in this example other than calling the .from_single_file() method to get the diffusion model.
