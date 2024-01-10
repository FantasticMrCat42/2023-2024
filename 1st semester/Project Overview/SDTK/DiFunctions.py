from diffusers import StableDiffusionPipeline, StableDiffusionXLPipeline, LCMScheduler
import torch
from datetime import datetime
import random
import logging
import os



logging.basicConfig(level=logging.INFO)


def save_img(image):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"outputs/output_image_{timestamp}.jpg"
    image.save(filename)
    return filename


def Fast_Mode(pipeline, lcm_lora_id):
    User_Steps = 8
    pipeline.load_lora_weights(lcm_lora_id)
    pipeline.scheduler = LCMScheduler.from_config(pipeline.scheduler.config)
    pipeline.to(device="cuda", dtype=torch.float16)
    return User_Steps




def Run_SDXL(Model_Id, User_Prompt, User_Negetive_Prompt,User_Steps ,User_Width, User_height, seed_value, Image_Count,User_Guidance_Scale, User_Fast_Mode):
    pipeline = StableDiffusionXLPipeline.from_single_file(
        Model_Id, torch_dtype=torch.float16, use_safetensors=True, HF_HUB_OFFLINE=True
    ).to("cuda")
    lcm_lora_id = "models\Loras\lcm_sdxl.safetensors"
    Fast_Mode(pipeline, lcm_lora_id)
    for i in range(Image_Count):  
        if seed_value == -1  or i >1:
            seed = int(random.randint(10000, 99999))
        print("User Prompt:", str(User_Prompt), " --seed: ", seed, "--Model", Model_Id)
        image = pipeline(
        prompt= User_Prompt,
        negative_prompt=User_Negetive_Prompt,
        num_inference_steps= Fast_Mode(pipeline, lcm_lora_id) if User_Fast_Mode == True else User_Steps,
        height=User_height,
        width=User_Width,
        generator = [torch.Generator(device="cuda").manual_seed(seed)],
        guidance_scale=User_Guidance_Scale,
        safety_checker=False
        ).images[0]
        img_path = save_img(image)
        print("finnished. Saved to: ", img_path)
        
        return img_path



def Run_SD_15(Model_Id, User_Prompt, User_Negetive_Prompt,User_Steps ,User_Width, User_height, seed_value, Image_Count,User_Guidance_Scale, User_Fast_Mode):
    pipeline = StableDiffusionPipeline.from_single_file(
        Model_Id, torch_dtype=torch.float16, use_safetensors=True
    ).to("cuda")
    lcm_lora_id = "models\Loras\lcm_sd15.safetensors"
    Fast_Mode(pipeline, lcm_lora_id)
    for i in range(5):  
        if seed_value == -1  or i >1:
            seed = int(random.randint(10000, 99999))
        print("User Prompt:", str(User_Prompt), " --seed: ", seed)
        image = pipeline(
        prompt= User_Prompt,
        negative_prompt=User_Negetive_Prompt,
        num_inference_steps= Fast_Mode(pipeline, lcm_lora_id) if User_Fast_Mode == True else User_Steps,
        height=User_height,
        width=User_Width,
        generator = [torch.Generator(device="cuda").manual_seed(seed)],
        guidance_scale=User_Guidance_Scale
        )#.images[0]

        print("finnished. Saved to: ", save_img(image))


#(Model_Id, User_Prompt, User_Negetive_Prompt,User_Steps ,User_Width, User_height, seed_value, Image_Count,User_Guidance_Scale, User_Fast_Mode)
Run_SDXL("models\SDXL_Turbo\dreamshaperXL_turboDpmppSDEKarras.safetensors","cat","",8,512,1024,-1,5,0.5, True)
#Run_SD_15("models\\SD_15\\revAnimated_v122.safetensors","a dog in a flip flops","",30,512,512,-1,1,3.5, False)
