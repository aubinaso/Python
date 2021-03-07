# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 01:32:18 2021

@author: aubin
"""

import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier("haar_face.xml")

people = ['donald', 'macron']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recogizer = cv.face.LBPHFaceRecognizer_create()
face_recogizer.read('face_trained.yml')

img = cv.imread('image/macron/macron2.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# Detect the face on the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    
    label, confidence = face_recogizer.predict(faces_roi)
    print('label ',people[label],' with a confidence of ',confidence)
    
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    
cv.imshow('Detected face', img)

cv.waitKey(0)