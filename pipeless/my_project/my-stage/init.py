import cv2

def init():
    return {
        "model": cv2.CascadeClassifier('/app/cats.xml') 
    }
