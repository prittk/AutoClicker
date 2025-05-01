import tkinter as tk
import ImageGraber
from PIL import ImageGrab, Image, ImageTk

def main_Gui():
    ##start main gui
    root = tk.Tk()
    root.title("AutoClicker")
    root.configure(background="grey")
    root.minsize(400,400)
    
    #grab screenshot of clicked area and pack for tk
    screenshot = ImageGraber.grabScreenshot()
    screenshot = Image.fromarray(screenshot)
    image = ImageTk.PhotoImage(screenshot)    
    
    
    tk.Label(root,image=image).pack()
    
    
    root.mainloop()


#start program
if __name__ == "__main__":
    main_Gui()
