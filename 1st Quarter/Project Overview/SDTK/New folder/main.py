from diffusers import StableDiffusionPipeline, StableDiffusionXLPipeline, LCMScheduler
import torch
import customtkinter
from DiFunctions import Run_SDXL
from threading import *
import time
import os
from PIL import ImageTk, Image
global imgPath
imgPath= "outputs\output_image_20231208164053.jpg"

models_folder = "models\SDXL"

finalCFG = 1
defaultCFG=1.5

model_paths = {}

for model_name in os.listdir(models_folder):
    if model_name.endswith(".safetensors"): 
        model_path = os.path.join(models_folder, model_name)
        model_paths[model_name] = model_path


root = customtkinter.CTk()
root.geometry("1200x500")
grey = "#2b2b2b"


customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")

def RunDif():
    print("WE STARTED WE STARTED WE STARTED WE STARTED WE STARTED WE STARTED WE STARTED WE STARTED WE STARTED WE STARTED WE STARTED WE STARTED WE STARTEDWE STARTEDWE STARTEDWE STARTEDWE STARTEDWE STARTEDWE STARTEDWE STARTED")
    selected_model = Model_Dropdown.get()
    model_path = model_paths[selected_model]
    for i in range(1):
        imgPath_ = Run_SDXL(model_path,entry1.get(0.0, 'end'),entry2.get(0.0, 'end'),30,int(Width_Entry.get()),int(Height_Entry.get()),-1,1,get_CFG_Entry(), False)
        print("yup my work here is done")
        tempImage = Image.open(imgPath_)
        w, h = tempImage.size
        ratio = 680/h
        new_height = 680
        new_width = int(w * ratio)
        tempImage = tempImage.resize((new_width, new_height))
        tempimg = ImageTk.PhotoImage(tempImage)
        panel.configure(image = tempimg)



def threading(): 
    # Call work function 
    t1= Thread(target=RunDif)
    t1.start() 


Upper_Frame = customtkinter.CTkFrame(root,  fg_color="transparent",)
Upper_Frame.grid(sticky='nw', row=0,column=0,padx=15, pady=15)

Left_Frame = customtkinter.CTkFrame(root, width=450,height=600)
Left_Frame.grid(sticky='nw', row=1,column=0, pady=0,padx=15)

Model_Frame = customtkinter.CTkFrame(Left_Frame, fg_color="transparent")
Model_Frame.grid(sticky='nw', row=0,column=0, pady=0,padx=15)

#Sampler_void = customtkinter.CTkLabel(Model_Frame,text='Model:',width=70)
#Sampler_void.grid(sticky='ne',pady=5,padx=5,row=0,column=0)

model_list = list(model_paths.keys())
Model_Dropdown = customtkinter.CTkComboBox(Model_Frame, values=model_list)
Model_Dropdown.grid(sticky='nw',pady=5,padx=5,row=0,column=1)

#Sampler_void = customtkinter.CTkLabel(Model_Frame,text='Sampler:',width=70)
#Sampler_void.grid(sticky='ne',pady=5,padx=5,row=0,column=2)

#Sampler_list = ['realisticVisionV51_v51VAE','juggernautXL_version2'] #FIX THIS
#Sampler_Dropdown = customtkinter.CTkComboBox(Model_Frame, values=Sampler_list)
#Sampler_Dropdown.grid(sticky='ne',pady=5,padx=5,row=0,column=3)

Width_Frame = customtkinter.CTkFrame(Left_Frame, fg_color="transparent")
Width_Frame.grid(sticky='nw', row=1,column=0, pady=0,padx=15)

Width_Entry = customtkinter.CTkEntry(Width_Frame,placeholder_text="width",width=90)
Width_Entry.grid(sticky='nw',pady=5,padx=5,row=1,column=0)

Width_slider = customtkinter.CTkSlider(Width_Frame, from_=0,to=100)
Width_slider.grid(sticky='nw',pady=12,padx=5,row=1,column=1)
Width_slider.configure(state="disabled")

#Width_list = ['512','768','1024'] #FIX THIS
#Width_Dropdown = customtkinter.CTkComboBox(Width_Frame, values=Width_list)
#Width_Dropdown.grid(sticky='nw',pady=5,padx=5,row=1,column=2)

Height_Frame = customtkinter.CTkFrame(Left_Frame, fg_color="transparent")
Height_Frame.grid(sticky='nw', row=2,column=0, pady=0,padx=15)

Height_Entry = customtkinter.CTkEntry(Height_Frame,placeholder_text="height",width=90)
Height_Entry.grid(sticky='nw',pady=5,padx=5,row=1,column=0)

Height_slider = customtkinter.CTkSlider(Height_Frame, from_=0,to=100)
Height_slider.grid(sticky='nw',pady=12,padx=5,row=1,column=1)
Height_slider.configure(state="disabled")

#Height_list = ['512','768','1024'] #FIX THIS
#Height_Dropdown = customtkinter.CTkComboBox(Height_Frame, values=Height_list)
#Height_Dropdown.grid(sticky='nw',pady=5,padx=5,row=1,column=2)

#seed = customtkinter.IntVar()
#seed.set(-1)

#def get_seed_Entry():
#    l= Seed_Entry.get()
#    return l

#Seed_Frame = customtkinter.CTkFrame(Left_Frame,fg_color="transparent")
#Seed_Frame.grid(sticky='nw', row=3,column=0, pady=0,padx=15)

#Seed_Entry = customtkinter.CTkEntry(Seed_Frame,placeholder_text="seed number",width=170, textvariable=seed)
#Seed_Entry.grid(sticky='nw',pady=5,padx=5,row=1,column=0)

#Seed_Entry_void = customtkinter.CTkLabel(Seed_Frame,text='',width=120)
#Seed_Entry_void.grid(sticky='ne',pady=5,padx=5,row=1,column=1)

#Seed_Check = customtkinter.CTkCheckBox(Seed_Frame, text='random seed')
#Seed_Check.grid(sticky='nw',pady=5,padx=5,row=1,column=2)

cfg_var = customtkinter.StringVar()
cfg_var.set(defaultCFG)

def get_CFG_Entry():
    e=(round((float(CFG_Entry.get()))*2)/2)
    return e


CFG_Frame = customtkinter.CTkFrame(Left_Frame, fg_color="transparent")
CFG_Frame.grid(sticky='nw', row=4,column=0, pady=0,padx=15)

CFG_Entry = customtkinter.CTkEntry(CFG_Frame,width=50, placeholder_text=defaultCFG, textvariable=cfg_var)
CFG_Entry.grid(sticky='nw',pady=5,padx=5,row=1,column=0)


CFG_slider = customtkinter.CTkSlider(CFG_Frame, from_=1, to=30, number_of_steps=60, width=145,)
CFG_slider.grid(sticky='nw',pady=12,padx=2,row=1,column=1)
CFG_slider.set(defaultCFG)

CFG_slider.configure(state="disabled")








Batch_Entry = customtkinter.CTkEntry(CFG_Frame,placeholder_text="Image count",width=90)
Batch_Entry.grid(sticky='nw',pady=5,padx=5,row=1,column=2)

#Batch_slider = customtkinter.CTkSlider(CFG_Frame, from_=0,to=4, width=150)
#Batch_slider.grid(sticky='nw',pady=12,padx=2,row=1,column=3)








my_Frame = customtkinter.CTkFrame(Upper_Frame)
my_Frame.pack()

#entry1_void = customtkinter.CTkLabel(my_Frame,text='positive prompt:',width=120)
#entry1_void.grid(sticky='nw',row=0,column=0)

entry1 = customtkinter.CTkTextbox(my_Frame, height=100, width=480)
entry1.grid(row=1, column=0,pady=5,padx=5,columnspan=3)

#entry2_void = customtkinter.CTkLabel(my_Frame,text='Negative prompt:',width=120)
#entry2_void.grid(sticky='nw',row=2,column=0)

entry2 = customtkinter.CTkTextbox(my_Frame, height=80, width=480)
entry2.grid(row=3, column=0,pady=5,padx=5,columnspan=3)

button = customtkinter.CTkButton(my_Frame, text="Submit", height=30, width=350, command=threading)
# Set sticky to 'ns' to make the button fill the vertical space)
button.grid(row=4, column=0,columnspan=3, sticky='nw', pady=5,padx=5)

#Style_list = ['style1','style2','style3'] #FIX THIS
#Style_Dropdown = customtkinter.CTkComboBox(my_Frame, values=Style_list, width=120)
#Style_Dropdown.grid(row=4, column=2, sticky='ne', pady=5,padx=5)

thing = customtkinter.CTkFrame(root,fg_color="transparent")
thing.grid(column=3,row=0, rowspan=10, pady=10)

#entry1_void = customtkinter.CTkLabel(my_Frame,text='positive prompt:',width=120)
#entry1_void.grid(sticky='nw',row=0,column=0)
panel = customtkinter.CTkLabel(thing,text='',height=460,width=460)
panel.grid()

#imageFrame = customtkinter.CTkFrame(root, width=460, height=460)
#imageFrame.grid(sticky='nw',columnspan=5, rowspan=4, row=0,column=2, pady=15,padx=10)

#Run_SDXL("models\SDXL_Turbo\RealitiesEdgeXLLCM_TURBOXL.safetensors","a dog in a flip flops","",4,1024,1024,-1,1,1.5, True)
 
root.mainloop()
