#screenshot function for ReadyGB
import cv2
import pyautogui
import numpy as np
from pynput import mouse

def pickRGB():  
    SS1 = returnSS() #initial screenshot cv2 object.
    cv2.imshow('Press any keyboard key to select the pixel under your cursor.', SS1)
    cv2.waitKey(0) #waits until key press or exiting window
    x, y = pyautogui.position() #x and y of mouse position
    SS2 = returnSS() #second screenshot that is accurate for x and y of mouse pos.
    cv2.destroyAllWindows() #destroys all windows opened by opencv
    
    return np.flip(SS2[y][x])


def returnSS(): #function that takes a ss and turns it into a np.array/opencv image object and returns it
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    return image
