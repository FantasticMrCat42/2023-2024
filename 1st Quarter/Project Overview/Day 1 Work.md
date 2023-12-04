## Note ##
today I plan to work on designing a good GUI on paper so that I can create it in Tkinter. Another important thing to note is I may inlcude a stable difusion video genorator because it was just released to to Diffusers pipline on huging face.

## GUI ##
I will first research other GUIs in the AI comunity so first i will include the most populer at least when I joined the community a year ago wich is the Automatic1111 stable diffusion webui (abrieviated as A1111).

### **[Automatic 1111 Stable diffuison Webui]** ###
this GUI was populer in the old Days of Open source AI image genoration becuase it was updated almost daily to keep up with the masive flood of AI news. In recent months it has fallen out of favor for more costomizable UIs like Comfy that uses a node system similer to parts blender. 

this is a link to the Open scource Webui: [A1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

the webui is not very beginer friendly but was the best option in the old days of AI (anything older than 6 months is considerd ancient). the webui sufferd from a plethera of instalation issues and a goal for my project is that my UI is much easier to launch and install without loosing the ability to directly accses the files like in A1111. the UI like almost all other stable diffusion GUIs usses gradio to create a webui but i will use tkinter so it can run as a window.

<img width="587" alt="image" src="https://github.com/FantasticMrCat42/2023-2024/assets/129550102/d367e814-0485-495f-bcb5-616d7ad8b851">

as you can see there are serveral tabs and inputs that make the GUI difficult for beginers and the settings menu is depicted bellow.
![127 0 0 1_7861_ (1)](https://github.com/FantasticMrCat42/2023-2024/assets/129550102/3e82e83c-e22a-45f4-b1b1-a74b3150d610)

as you can see its unresonable.

ive learned from this UI that most of these features are badly implimented for UX and could be changed. an example is the resolution settings because stable diffusion only works well with certan asspect ratios and the slider does not reflect that or have many options for aspect ratios. admitidly the UI does have very good functionality with extentions wich my UI will defenatly not.

### **[Comfy UI]** ###
this UI is unique in the fact that it is Node based and the user creates there own workflow. in my case I wont be able to create anything like this so I was unable to parce much from it. 

simple workflow in comfy UI:
<img width="935" alt="image" src="https://github.com/FantasticMrCat42/2023-2024/assets/129550102/4dbdc273-2ee8-4103-a1af-8280815876f0">


this one is more complex:
![image](https://github.com/FantasticMrCat42/2023-2024/assets/129550102/45182bc4-4cf2-4486-9e71-987369775f7c)






this creates an enviroment that is easy for users to make the ui that works for them perfictly but making you own workflow can be complex.
the UI does have a very simple folder for its settings that abstracts alot from the user but still makes it easily accsesable.
<img width="519" alt="image" src="https://github.com/FantasticMrCat42/2023-2024/assets/129550102/f2be2ef8-1cd2-44bf-87fe-6e292f7f84ae">

### **[Fooocus UI]** ###
this Webui (also using the gradio library) is the pinicle of simplicity and only shows the users advanced options when they want it. in my opinion this is a oposing extreme to th A1111 UI and feals to limiting to the user. on the other hand it has a extreamly good selection of premade styles with pre-writen promt enhansers that make literaly any image look good unlinke with A1111 where you need to deticate hours to make a good image. i want my UI to strike a balance between being easy to use and controlable while still being able to make the image i image with more costomization to my image

this is the webui:
<img width="1170" alt="image" src="https://github.com/FantasticMrCat42/2023-2024/assets/129550102/2c93ea19-c5e8-4ddb-92fd-d9d8a544f094">

this is the webui with advanced settings:
<img width="1138" alt="image" src="https://github.com/FantasticMrCat42/2023-2024/assets/129550102/922a72a6-bddc-4533-b5f0-e74d101b3a31">


the advanced version is simmiler to what I am aiming for and it does solve many of the problems I had like not knowing what resolutions i can pick but it abstracts Way to much from the user and hidners the creative prosses.

### **[Fooocus UI]** ###
this is a UI i have never used but have come across in the past. its a good balance and looks like what I am aiming for: 
![image](https://github.com/FantasticMrCat42/2023-2024/assets/129550102/33909c28-198b-463f-a94e-d96b6a87ab6e)


