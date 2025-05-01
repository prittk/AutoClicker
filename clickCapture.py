from pynput.mouse import Listener
import time

mouseClickPost = []

def grabClickPost():
    global mouseClickPost
    with Listener(on_click=clicked) as listener:
        Post = listener.join()
        
    return mouseClickPost
         
        
def clicked(x,y,button,pressed):
    global mouseClickPost
    if pressed:
        mouseClickPost = [x,y]
        print(x,y)
        return False
    
