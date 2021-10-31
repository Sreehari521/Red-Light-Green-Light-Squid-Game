import cv2
import winsound
import pyttsx3
import random

cam = cv2.VideoCapture(0)

def talk(txt):
    r = pyttsx3.init()
    r.say(txt)
    r.runAndWait()

while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    val = random.choice(["green", "red"])
    talk(val)

    if val == "green":
        if cv2.waitKey(10) == ord('q'):
            break

    if val == "red":
        for c in contours:
            if cv2.contourArea(c) < 5000:
                continue

            x, y, w, h = cv2.boundingRect(c)
            if cv2.waitKey(10) == ord('q'):
                break
            
            winsound.PlaySound('alert.wav', winsound.SND_ASYNC)