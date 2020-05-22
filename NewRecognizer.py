import cv2
import numpy as np
import os
import time
from datetime import date
import UpdateAttendance

recognizer1 = cv2.face.LBPHFaceRecognizer_create()
recognizer1.read('Scripts/Trainer/FacultyTrainer.yml')

recognizer2 = cv2.face.LBPHFaceRecognizer_create()
recognizer2.read('Scripts/Trainer/trainer.yml')

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

id1 = 0
id2 = 0

# names related to ids: example ==> Shreya: id=1,  etc
names = ['None','Shreya','Siddhi','Manjiri','Aastha','Somesh']
subjects = ['None','AI','CG','DBMS','ADS']

cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video widht
cam.set(4, 480)  # set video height

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

today = date.today()
date = today.strftime("%d/%m/%Y")
#subject=1

print("Recognizing subject...")
ch=1
while (ch!=0):
    ret, img = cam.read()
    img = cv2.flip(img, 1)  # Flip vertically

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=2,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id1, confidence = recognizer1.predict(gray[y:y + h, x:x + w])
        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 100):
            subject=id1
            print(subjects[subject])
            confidence = "  {0}%".format(round(100 - confidence))
            cv2.putText(img, str(subject), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            time.sleep(2)
            ch=0

    cv2.imshow('camera', img)
    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break

UpdateAttendance.setDefault(date, subject)
while True:

    ret, img = cam.read()
    img = cv2.flip(img, 1)  # Flip vertically

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        id2, confidence = recognizer2.predict(gray[y:y + h, x:x + w])

        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 100):
            UpdateAttendance.update(date, subject, id2)
            name = names[id2]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            name = "Unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(name), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        #cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff  #Press 'ESC' for exiting video
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()
