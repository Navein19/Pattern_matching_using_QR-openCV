# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 09:44:01 2019

@author: Navein Kumar
"""

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

import winsound
frequency = 2500
freq1=4000  # Set Frequency To 2500 Hertz
duration = 33 
duration1=500
ctr=1
detected=0
 # Set Duration To 1000 ms == 1 second


cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        #print("Data", obj.data)
        dat = str(obj.data)
        cv2.putText(frame, dat, (50, 50), font, 2,
                    (255, 0, 0), 3)
        
        concats= "b'"+str(ctr)+"'"
        concats1="b'"+str(ctr-1)+"'"
        if(dat==concats):
            winsound.Beep(freq1, duration1)
            detected=1
            ctr=ctr+1
            
        elif (dat==concats1 and detected==1):
            
            continue
        
        elif dat!=concats:
            winsound.Beep(frequency, duration)
            
            #winsound.PlaySound('C:/Users/Navein Kumar/Desktop/nokia proj 2/sound1.wav', winsound.SND_FILENAME)
        
    
        

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    
    
print(ctr)

cap.release()

cv2.destroyAllWindows()    