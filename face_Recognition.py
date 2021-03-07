# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 00:17:38 2021

@author: aubin
"""
import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

people = ['donald', 'macron']
DIR = r'image/'
haar_cascade = cv.CascadeClassifier("haar_face.xml")

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            for (x,y,w,h) in faces_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()
# print('Length of the features ',len(features))
# print('Length of the features ',len(labels))

face_recognizer = cv.face.LBPHFaceRecognizer_create()

features = np.array(features, dtype='object')
labels = np.array(labels)

# Train the Recognizer on the features list and the labels list

face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

# p = []
# img = cv.imread("image/macron1.png")
# cv.imshow("image", img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray )

# for i in os.listdir('image'):
#     p.append(i)
    
# print(p)

cv.waitKey(0)