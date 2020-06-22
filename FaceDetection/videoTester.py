import cv2
import os
import numpy as np
import faceRecognition as fr
import database as db
import random

def save_frame_image(count):
        cv2.imwrite("SavedImages/frame%d.jpg"%count,test_img)

def convert_to_binary(filename):
    with open(filename ,'rb') as file:
        bniaryData = file.read()
    return bniaryData
    
'''
faces , faceID = fr.labels_for_traning_data("TraningImages")
face_recognizer = fr.train_classifier(faces,faceID)
#here we save our traning data of recognizer....
face_recognizer.save("traning_data.yml")

'''
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("traning_data.yml")

name = {0:"nbbhatt",1:"anjali"}

cap = cv2.VideoCapture(0)

while True:
    ret ,test_img = cap.read()
    faces_detected,gray_img = fr.faceDetection(test_img)

    for (x,y,w,h) in faces_detected:
        cv2.rectangle(test_img,(x,y),(x+y,y+h),(255,0,0),thickness=3)

    resized_img = cv2.resize(test_img,(1000,700))
    cv2.imshow("face_detection_tutorial",resized_img)
    cv2.waitKey(10)

    for face in faces_detected:
        (x,y,w,h) = face
        roi_gray = gray_img[y:y+h,x:x+w]
        label,confidence = face_recognizer.predict(roi_gray)
        print("confidence : ",confidence)
        print("label : ",label)
        fr.draw_rect(test_img,face)
        predicted_name = name[label]
        if (confidence < 45   ):
            fr.put_text(test_img,predicted_name,x,y)
            count = random.randrange(0,1000000)
            save_frame_image(count)
            file = convert_to_binary('SavedImages/frame%d.jpg'%count)
            db.connect_database(predicted_name,file)
        
    resized_img = cv2.resize(test_img,(1000,700))
    cv2.imshow("face_detection_tutorial",resized_img)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows
    
        
