import cv2
import os

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id = input('Enter your id:')
sampleNum = 1
os.chdir(r'C:\Users\Somesh Rathi\PycharmProjects\AutomaticAttendance\venv\Scripts\Dataset')
while (True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imwrite("Student.{0}.{1}.jpg".format(Id, str(sampleNum)), gray[y:y + h, x:x + w])
        sampleNum = sampleNum + 1
        #cv2.imshow('frame', img)
    if cv2.waitKey(300) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum > 30:
        break
cam.release()
cv2.destroyAllWindows()