import cv2
import os
import numpy as np
import faceRecognition as fr

test_img = cv2.imread('TestImages/s1.jpg')
faces_detected,gray_img = fr.faceDetection(test_img)
print("deteced face: ",faces_detected)

#faces , faceID = fr.labels_for_traning_data("TraningImages")
#face_recognizer = fr.train_classifier(faces,faceID)
#here we save our traning data of recognizer....
#face_recognizer.save("traning_data.yml")

#here we loading that traing data ,so there is no need of above 3 commented lines becz we trained model already.....
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("traning_data.yml")

#label a/c to id..........
name = {0:"nbbhatt"}

for face in faces_detected:
    (x,y,w,h) = face
    roi_gray = gray_img[y:y+h,x:x+w]
    label,confidence = face_recognizer.predict(roi_gray)
    print("confidence : ",confidence)
    print("label : ",label)
    fr.draw_rect(test_img,face)
    predicted_name = name[label]
    if (confidence > 37):
        continue
    fr.put_text(test_img,predicted_name,x,y)

resized_img = cv2.resize(test_img,(1000,700))
cv2.imshow("face_detection_tutorial",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows
    


