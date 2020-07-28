import cv2
import tkinter as tk #package which is used for creating gui
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') # cascade
function for eye detection.
face_cascade =
cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # cascade
function for face detection.
#This function detects eyes and face in a still image.
def imageDetection():
img = cv2.imread("abc.jpg")
cv2.imshow('Original',img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray,scaleFactor =
1.1,minNeighbors = 20)
faces =
face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors = 9)

for x,y,w,h in eyes:
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.putText(img, 'eyes', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5,
(0, 0, 0))
for x,y,w,h in faces:
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.putText(img, 'face', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5,
(0, 0, 0))
cv2.imshow('Gray', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# This function detects eyes and face in a live video captured through
the user's webcam.
def videoDetection():
cap = cv2.VideoCapture(0)
while True:
ret,frame = cap.read()
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray,1.1,20)
face = face_cascade.detectMultiScale(gray, scaleFactor=1.1,
minNeighbors=9)
for x, y, w, h in eyes:
frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0,
255, 0),5)
cv2.putText(frame,'eyes',(x,y),
cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0))

for x, y, w, h in face:

frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0,

255),5)

cv2.putText(frame, 'face', (x, y), cv2.FONT_HERSHEY_COMPLEX,

1, (255, 0, 0))
cv2.imshow('Output2', frame)
if cv2.waitKey(1) == 13:
break
cap.release()
cv2.destroyAllWindows()
#main function

if __name__ == '__main__':
r = tk.Tk()
r.geometry("200x50")
r.title('Operations')
button = tk.Button(r, text='Image Detection', width=25,
command=imageDetection)
button1 = tk.Button(r, text='Video Detection', width=25,
command=videoDetection)
button.pack()
button1.pack()
r.mainloop()