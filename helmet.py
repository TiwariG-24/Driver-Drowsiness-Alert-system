import queue,threading,time
import cv2
import numpy
from playsound import playsound

input_buffer = queue.Queue()
input_buff = queue.Queue()
face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml',)       # Load the cascade
cap = cv2.VideoCapture(0)                                   # To capture video from webcam.
flag = 0

def processing():
    while True:
        img =input_buffer.get()
        cv2.imshow("img", img)                              # Display
        time.sleep(0.025)
        k = cv2.waitKey(1)                                  # Stop the program
        if k == ord('q'):
            break
    return

def processed():                                            # Play audio depending on the inputs
    while True:
        global flag

        fram = input_buff.get()
        if type(fram)==tuple:
            flag=flag+1
        if isinstance(fram, numpy.ndarray):
            flag=0
        if flag>=10:
            playsound('Alarm.wav')
            print("1")
            flag=0
            time.sleep(0.025)
    return

def pro():
    while True:
        fra = input_buff.get()
        if isinstance(fra, numpy.ndarray):
          for (x, y, w, h) in fra:
                cv2.rectangle(img, (x, y), (x + w, x + h), (255,0,0), 2)            # Draw the rectangle around the object
        time.sleep(0.025)
    return

t = threading.Thread(target=processing)
t2 = threading.Thread(target=processed)
t3 = threading.Thread(target=pro)
t.start()
t2.start()
t3.start()

while True:
        _,img = cap.read()                                                              # Read the frame
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                    # Convert to grayscale
        face = face_cascade.detectMultiScale(gray, 1.01, 25)         # Detect the eyes
        input_buff.put(face)
        input_buffer.put(img)
        time.sleep(0.025)
cap.release()                                                                           # Release the VideoCapture object
