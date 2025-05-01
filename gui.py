import tkinter as tk
import ImageGraber
from PIL import ImageGrab, Image, ImageTk
import time


def main_Gui():
    ##start main gui
    root = tk.Tk()

    root.title("AutoClicker")
    root.configure(background="grey")
    root.minsize(400,400)
    
    
    #grab screenshot of clicked area and pack for tk
    
    screenshotButton = tk.Button(root, text="Get Cickable", command =lambda: screenshot(root))
    screenshotButton.pack()
    
    #add a button to start screenshot capture
    
    
    root.mainloop()
    
def screenshot(root):
    print("button clicked")
    screenshot = ImageGraber.grabScreenshot()
    screenshot = Image.fromarray(screenshot)
    image = ImageTk.PhotoImage(screenshot)
    label = tk.Label(root,image=image)
    label.image = image
    label.pack()

    


#start program
if __name__ == "__main__":
    main_Gui()
    

