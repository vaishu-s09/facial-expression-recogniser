import cv2
import numpy as np
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#faceDetect=cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)

#if(CascadeClassifier.Load(xmlFile)):
    #print("Error reading cascade file: %v\n", xmlFile)



while(True):
    ret,img=cam.read()
    print(ret)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("FACEDETECTIONPT1",img)
    if(cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroAllWindows()



      
  
