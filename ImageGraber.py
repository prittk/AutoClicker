import numpy
import cv2
import pytesseract 
from PIL import ImageGrab
import clickCapture as cc


#make a screenshot of the click in a box and display 
def grabScreenshot():
    
    clickedPost = cc.grabClickPost()
    print(clickedPost)
    box = drawBox(clickedPost)
    
    captureScreen = numpy.array(ImageGrab.grab(bbox=(box[0],box[1],box[2],box[3])))
    screenshot = cv2.cvtColor(captureScreen,cv2.COLOR_BGR2RGB)
  
    
    
    return screenshot

        
def drawBox(mousePost):
    x = mousePost[0]-100 ##left point x
    y = mousePost[1]-100 ## bottom point y
    w = mousePost[0]+100
    h = mousePost[1]+100
    ##   x,y,w,h for screenshot 200x200 pixel size
    boxTarget = [x, y, w, h]
    print(boxTarget)
    
    return boxTarget
        
    
grabScreenshot()
    