#importing libraries 
import cv2
import imutils
import numpy as np
import os

#calling the pre-trained model for human detection (implemented in opencv with SVM)
HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#function to detect per frame
def detect(frame):
    bounding_box_cordinates, weights =  HOGCV.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 1.03)
    
    person = 1
    for x,y,w,h in bounding_box_cordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f'person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        person += 1
    
    cv2.putText(frame, 'Status : Detecting ', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0,255,0), 2)
    cv2.putText(frame, f'Total Persons : {person-1}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0,255,0), 2)
    cv2.imshow('Output', frame)

    return frame

#frames are combined to detect in a video
def detect_Video(path):

    video = cv2.VideoCapture(path)
    check, frame = video.read()
    if check == False:
        print('Video not found as invalid path entered.')
        return

    print('Detecting people...')
    while video.isOpened():
        #check is True if reading was successful 
        check, frame =  video.read()

        if check:
            frame = imutils.resize(frame , width=min(800,frame.shape[1]))
            frame = detect(frame)
            
            key = cv2.waitKey(1)
            if key== ord('q'):
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()


def detect_Camera():   
    video = cv2.VideoCapture(0)
    print('Detecting people...')

    while True:
        check, frame = video.read()

        frame = detect(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
                break

    video.release()
    cv2.destroyAllWindows()

#single image is treated as a frame
def detect_Image(path):
    image = cv2.imread(path)

    image = imutils.resize(image, width = min(800, image.shape[1])) 

    result_image = detect(image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

#call functions as per the file type
def human_detector(path,file):
    
    if file=='Image':
        print('[INFO] Opening Image from path.')
        detect_Image(path)
    if file=='Video':
        print('[INFO] Opening Video from path.')
        detect_Video(path)
    if file=='Camera':
        print('[INFO] Opening Web Cam.')
        detect_Camera()


