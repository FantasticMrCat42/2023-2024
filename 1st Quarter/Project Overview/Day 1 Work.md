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
### **[Comfy UI]** ###

ive learned from this UI that most of these features are badly implimented for UX and could be changed. an example is the resolution settings because stable diffusion only works well with certan asspect ratios and the slider does not reflect that or have many options for aspect ratios. admitidly the UI does have very good functionality with extentions wich my UI will defenatly not.

