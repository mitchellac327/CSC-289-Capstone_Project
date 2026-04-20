"""SIMPLE HAIRCUT CHANGER - Use Your Own Photo"""

import os
import replicate
import sys

import time
import datetime
import getpass
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo



from pathlib import Path

prompt = ""
hairStyle = None
beardStyle = None
color = None
        



def mainMenu():
        def imageUpload(filePath):

            # Check if file exists
            if not os.path.exists(filePath):
                print(f"\n❌ File not found: {filePath}")
                showinfo(
                    title='Error',
                    message="File Not Found!")
                exit()


            print(f"✅ Found: {filePath}")
            showinfo(
                    title='Image Selected',
                    message="Image found succesfully!")
            return filePath

        def chooseService(service, hairStyle, beardStyle, isDone):
            if service == "Normal Haircut" and hairStyle is not None:
                prompt += "Replace my current hair with " + hairStyle
                

                
                
                isDone = True


                print(f"✅ Service: A hairstyle with {hairStyle}")
            elif service == "Haircut And Beard Trim" and hairStyle is not None and beardStyle is not None:
                beardStyle = input("Describe the beard trim you want (Note: Don't use complete sentences): ")
                prompt += "Replace my current hair with " + hairStyle + " and for the beard, replace it with " + beardStyle + ". "
                print(f"✅ Service: A hairstyle with {hairStyle}  and a beard trim of {beardStyle}")
                isDone = True

            elif service == "Beard Trim" and beardStyle is not None:
                prompt += "Replace my current beard with " + beardStyle
                print(f"✅ Service: A beard trim of {beardStyle}")
                isDone = True

            else:
                exit()
        mainMenuWin = Tk()
        mainMenuWin.geometry("420x420")
        mainMenuWin.title("Haircut AI Image Generator")
        mainMenuWin.config(bg="#0011ff") 

        #icon = PhotoImage(file='.png')
        #mainMenuWin.iconphoto(True, icon)

        l = Label(mainMenuWin, text = "🎨 HAIRCUT CHANGER - USE YOUR OWN PHOTO")
        l.config(font =("Courier", 14))
        l.pack()

        filename = None

        def select_file():
            filetypes = (
                ('jpg', '*.jpg'),
                ('All files', '*.*')
            )

            filename = fd.askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=filetypes)

            showinfo(
                title='Selected File',
                message=filename)
            
            filename = imageUpload(filename)  
            return filename

        filename = select_file()        




        mainMenuWin.hairStyle = ["No Hair Change", "Fade", "Taper", "Buzz Cut", "Curly", "Dreads", "Other"]
        mainMenuWin.option_hs = StringVar(mainMenuWin)
        mainMenuWin.option_hs.set("Choose Hairstyle")
        entry_box_hs = None

        def option_changed_hs(value):
            global prompt
            global hairStyle 
            print("Selected Hairstyle:", value)
            hairStyle = value
            if hairStyle == "Other":
                lbl = Label(mainMenuWin, text="Enter Hairstyle:")
                entry_box_hs = Entry(mainMenuWin, width=30)
                entry_box_hs.pack(pady=10)
                    
        option_menu_hs = OptionMenu(
            mainMenuWin,
            mainMenuWin.option_hs,
            *mainMenuWin.hairStyle,
            command=option_changed_hs)
        option_menu_hs.pack(pady=10)
        
        
        



        mainMenuWin.beardStyle = ["No Beard Change", "Short Boxed", "Stubble", "Beard Fade", "Full Beard", "Circle Beard", "Other"]
        mainMenuWin.option_bs = StringVar(mainMenuWin)
        mainMenuWin.option_bs.set("Choose Beardstyle")
        entry_box_bs = None

        def option_changed_bs(value):
            global prompt
            global beardStyle
            print("Selected Beardstyle:", value)
            beardStyle = value
            if beardStyle == "Other":
                lbl = Label(mainMenuWin, text="Enter Beard Style:")
                entry_box_bs = Entry(mainMenuWin, width=30)
                entry_box_bs.pack(pady=10)

                    
        option_menu_bs = OptionMenu(
            mainMenuWin,
            mainMenuWin.option_bs,
            *mainMenuWin.beardStyle,
            command=option_changed_bs)
        option_menu_bs.pack(pady=10)
        
        mainMenuWin.color = ["No Color Change" ,"Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Brown", "Black", "Other"]
        mainMenuWin.option_co = StringVar(mainMenuWin)
        mainMenuWin.option_co.set("Choose Color (Optional)")
        entry_box_co = None

        def option_changed_co(value):
            global color
            global prompt
            print("Selected Color:", value)
            color = value
            if color == "Other":
                lbl = Label(mainMenuWin, text="Enter Color:")
                entry_box_co = Entry(mainMenuWin, width=30)
                entry_box_co.pack(pady=10)
            
                    
        option_menu_co = OptionMenu(
            mainMenuWin,
            mainMenuWin.option_co,
            *mainMenuWin.color,
            command=option_changed_co)
        option_menu_co.pack(pady=10)


      


        reportsAndAnalyticsBtn = Button(mainMenuWin, text="Generate Image", font=("Arial", 16), bg="#d4ff00", fg="black", padx=10, pady=5, command=lambda: ())
        reportsAndAnalyticsBtn.config(command=lambda: clickedGenerateButton(prompt, hairStyle, beardStyle, color, filename, entry_box_bs, entry_box_hs, entry_box_co))
        reportsAndAnalyticsBtn.pack(pady=10)
           

        #Generate the API
        def clickedGenerateButton(prompt, hairStyle, beardStyle, colorOption, image_path, berardTextBox, hairTextBox, colorTextBox):

            if hairStyle == "Other":
                hairStyle = hairTextBox.get()
            if hairStyle != "No Hair Change" and hairStyle != None and hairStyle != "Choose Beardstyle":
                prompt += "Replace my current hair with a " + hairStyle + " style. "
            
            if beardStyle == "Other":
                beardStyle = berardTextBox.get()
            if beardStyle != "No Beard Change" and beardStyle != None and beardStyle != "Choose Beardstyle":
                prompt += "Replace my current beard with a " + beardStyle + " style. "
              
            if colorOption == "Other" and colorTextBox is not None:
                colorOption = colorTextBox.get()
            if colorOption != "No Color Change" and colorOption != None and colorOption != "Choose Color (Optional)":
                prompt += "Change the hair color to a " + colorOption + " color. "
            


            final_prompt = "Modify the hairstyle in the uploaded image. Keep my face, expression, and skin tone unchanged. " + prompt + " Ensure the new hair looks realistic and matches the lighting, shadows, and perspective of the original photo. Do not change the background, head size, or any other part of the image."
            
            print("The AI image is being prompted.")
            print("The Prompt: " + final_prompt)
            print("\n" + "="*70)
            print(f"📸 Input: {final_prompt}")
            if hairStyle != None and hairStyle != "No Hair Change" and hairStyle != "Choose Beardstyle":
                print(f"💇 Hair Style: {hairStyle}")
            if beardStyle != None and beardStyle != "No Beard Change" and beardStyle != "Choose Beardstyle":
                print(f"💇 Beard Style: {beardStyle}")
            if colorOption != 'No Color Change' and colorOption != None and colorOption != "Choose Color (Optional)":
                print(f"🎨 Color: {colorOption}")
            print("="*70)
            generateoption = input("Are you ready to generate? (yes/no)").lower().strip()
            if generateoption == 'yes':
                print("\nGenerating...")
                print("\n🚀 Generating AI Image...")

                try:
                    # Open the image file and upload it
                    with open(image_path, "rb") as img:
                            output = replicate.run(
                            "black-forest-labs/flux-2-pro",
                            input={
                                "prompt" : final_prompt, 
                                "resolution": "match_input_image",
                                "aspect_ratio": "match_input_image",
                                "input_images": [img],
                                "output_format": "jpg",
                                "output_quality": 80,
                                "safety_tolerance": 2
                            }
                        )
                    
                    print("\n✅ SUCCESS!")
                    print(f"🔗 View online: {output}")
                    
                    
                    download = input("\n💾 Download and save the result? (yes/no): ").lower().strip()
                    
                    if download == "yes":
                        print("\n📥 Downloading...")
                        
                        # Create output folder
                        output_dir = Path("my_hairstyles")
                        output_dir.mkdir(exist_ok=True)
                        
                        # Download image
                        response = requests.get(output)
                        
                        if response.status_code == 200:
                            # Create filename
                            original_name = Path(image_path).stem
                            output_filename = f"{original_name}_{hairStyle.replace(' ', '_')}.png"
                            output_path = output_dir / output_filename
                            
                            # Save file
                            with open(output_path, "wb") as f:
                                f.write(response.content)
                            
                            print(f"\n✅ AI Image Saved!")
                            print(f"📁 Location: {output_path.absolute()}")

                        else:
                            print(f"❌ Download failed (HTTP {response.status_code})")
                    
                    
                except FileNotFoundError:
                    print(f"\n❌ Error: Could not find file '{image_path}'")
                    
                except replicate.exceptions.ReplicateError as e:
                    print(f"\n❌ Replicate API Error: {e}")
                    print("\nPossible issues:")
                    print("- Invalid API token")
                    print("- Insufficient credits")
                    print("- Image format not supported")
                    
                except Exception as e:
                    print(f"\n❌ Error: {e}")
                    print(f"Error type: {type(e).__name__}")

            
        
                
        mainMenuWin.mainloop()
# Set your API token
try:
    with open('.env', 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    if key == 'REPLICATE_API_TOKEN':
                        api_token = value
                        break
except Exception as e:
    print(f"ERR: Failed to read .env: {e}")
    input("\nPress Enter to exit...")
    sys.exit(1)

os.environ["REPLICATE_API_TOKEN"] = api_token

print("="*70)
print("🎨 HAIRCUT CHANGER - USE YOUR OWN PHOTO")
print("="*70)

mainMenu()

# ============================================================================
# STEP 5: Generate!
# ============================================================================



input("\nPress Enter to exit...")