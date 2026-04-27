# This program is designed for Swift to use the Replicate API to generate images based on user input.
# NOTE: This program must include an .env file with a REPLICATE_API_TOKEN variable that contains your Replicate API token in order for the image generation to work. 

import tkinter as tk
from tkinter import *
import os
import replicate
from dotenv import load_dotenv
load_dotenv()




def main_menu():
    prompt = ""
    hairStyle = None
    beardStyle = None
    hairColor = None
    isDone1 = False
    isDone2 = False
    isDone3 = False
    # STEP 1: Upload Image
    print("""This program is designed for Swift to use the Replicate API to generate images based on user input.
NOTE: This program must include an .env file with a REPLICATE_API_TOKEN variable that contains your Replicate API token in order for the image generation to work.""")
    filePath = input("Enter image path (It must be under 2048x2048 resolution and in PNG, JPG, JPEG, or WEBP format): ")
    imagePath = imageUpload(filePath)

    # STEP 2: Choose Service
    service = input("Choose a service (Normal Haircut, Haircut And Beard Trim, Beard Trim): ")
    if service == "Normal Haircut":
        isDone1 = True

    elif service == "Haircut And Beard Trim":
        isDone1 = True

    elif service == "Beard Trim":
        isDone1 = True

    else:
        print("Make sure you have spelled the listed services correctly.")
        exit()

    # STEP 3: Choose Hair Style
    if isDone1:
        if service == "Normal Haircut" or service == "Haircut And Beard Trim":
            hairStyle = input("Describe the hairstyle you want (Note: Don't use complete sentences): ")
            prompt += "Replace my current hair with " + hairStyle + "."
            print(f"Service: A hairstyle with {hairStyle}")
            isDone2 = True
        if service == "Beard Trim" or service == "Haircut And Beard Trim":
            beardStyle = input("Describe the beard trim you want (Note: Don't use complete sentences): ")
            prompt += "Replace my current beard with " + beardStyle + "."
            print(f"Service: A beard trim of {beardStyle}")
            isDone2 = True

    # Step 4: Choose Hair Color
    if isDone2:
        colorOption = input("Do you want to change your hair color? (Yes/No): ")
        if colorOption.lower() == "yes":
            hairColor = input("Describe the hair color you want (Note: Don't use complete sentences): ")
            prompt += "Change my current hair color to " + hairColor + "."
            print(f"Service: A hairstyle with {hairStyle} and a hair color of {hairColor}")
            isDone3 = True
        elif colorOption.lower() == "no":
            isDone3 = True
        else:
            exit()

    prompt += " Keep the background and everything else the same."
    print("Final Prompt: " + prompt)
    input("Are you ready to generate the image? (Press Enter to continue or Ctrl + C to exit)")
    generateImage(prompt, imagePath, isDone1, isDone2, isDone3)

def generateImage(final_prompt, img, isDone1, isDone2, isDone3):
    if isDone1 and isDone2 and isDone3:
        
        print("Generating image...")
        try:
            with open(img, "rb") as image:
                output = replicate.run(
            "black-forest-labs/flux-2-pro",
            input={
                    "prompt" : final_prompt,
                    "resolution": "match_input_image",
                    "aspect_ratio": "match_input_image",
                    "input_images": [image],
                    "output_format": "jpg",
                    "output_quality": 80,
                    "safety_tolerance": 2
            }
        )
            print("Image generated successfully.")
        except Exception as err:
            print("Error generating image: " + str(err))
            exit()
    else:
        print("Critical Error: Not all steps were completed successfully.")
        exit()

def imageUpload(filePath):
    if not os.path.isfile(filePath):
        print("Image does not exist.")
        exit()
    elif not filePath.lower().endswith(('.png', '.jpg', '.jpeg', 'webp')):
        print("Invalid file type. Please upload a PNG, JPG, JPEG, or WEBP image.")
        exit()
    #elif filePath.lower().resolution > (2048, 2048):
     #   print("Image resolution exceeds 2048x2048.")
      #  exit()
    else:
        print("Image uploaded successfully.")
        return filePath
    
main_menu()