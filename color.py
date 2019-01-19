# import the necessary packages
from pyautogui import press
import numpy as np
import argparse
import cv2

from collections import deque
from imutils.video import VideoStream
import imutils
import time

<<<<<<< HEAD
# Detector functions
def jump(pointsG , pointsR):
    minyG = 0
    maxyG = 0
    minyR = 0
    maxyR = 0
    if len(pointsG) > 0:
        minyG = pointsG[0][0]
        maxyG = pointsG[0][1]

    if len(pointsR) > 0:
        minyR = pointsR[0][0]
        maxyR = pointsR[0][1]

    for pxy in pointsG:
        if pxy[1] < minyG:
            minyG = pxy[1]
        if pxy[1] > maxyG:
            maxyG = pxy[1]

    for pxy in pointsR:
        if pxy[1] < minyR:
            minyR = pxy[1]
        if pxy[1] > maxyR:
            maxyR = pxy[1]
    # print(maxy - miny)

    if (maxyR - minyR > 200) or (maxyG - minyG > 200):
        return True
        #pointsG.clear()
=======
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
>>>>>>> 3759948ee7ff67740e18ddc1106a1d901fd91e72


# define the list of boundaries
boundaries = [
	([89, 182, 0], [255, 255, 162])
]

boundariesLab = [
	([ 0, 0, 0], [255, 120, 255]),([ 0, 175, 0], [255, 255, 255])
]


vs = VideoStream(src=0).start()
time.sleep(2.0)

pointsG = []
pointsR = []


while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    frame = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)

    i = 0
    # loop over the boundaries

    # create NumPy arrays from the boundaries
    lowerG = np.array([ 0, 0, 0], dtype = "uint8")
    upperG = np.array([255, 120, 255], dtype = "uint8")

    lowerR = np.array([ 0, 163, 0], dtype = "uint8")
    upperR = np.array([255, 255, 255], dtype = "uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    maskG = cv2.inRange(frame, lowerG, upperG)
    maskR = cv2.inRange(frame, lowerR, upperR)
    maskG = cv2.erode(maskG, None, iterations=2)
    maskG = cv2.dilate(maskG, None, iterations=2)
    maskR = cv2.erode(maskR, None, iterations=2)
    maskR = cv2.dilate(maskR, None, iterations=2)

    centxG = 0
    centyG = 0
    centyR = 0
    centxR = 0
    contoursG , h = cv2.findContours(maskG ,cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    contoursR, h = cv2.findContours(maskR, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contoursG:
        area = cv2.contourArea(contour)
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(frame , [box] ,0 ,(0,0,255) ,2)

        print("rectangle")
        print(rect)
        #print(area)
        if area > 2000:
            M = cv2.moments(contour)
            if(len(pointsG) > 30):
                print(pointsG)
                pointsG.pop(0)
            pointsG.append((M['m10'] / M['m00'] ,M['m01'] / M['m00'] ))
            centxG = M['m10'] / M['m00']
            centyG = M['m01'] / M['m00']
            break
    for contour in contoursR:
        area = cv2.contourArea(contour)
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)

        #print(len(contour[0]))
        # print(area)
        if area > 2000:
            M = cv2.moments(contour)
            if (len(pointsR) > 30):
                pointsR.pop(0)
            pointsR.append((M['m10'] / M['m00'], M['m01'] / M['m00']))
            centxR = M['m10'] / M['m00']
            centyR = M['m01'] / M['m00']
        break

<<<<<<< HEAD
    if jump(pointsG , pointsR) == True:
        print("JUMP")
    # Detection checks

=======
    miny = pointsG[0][0]
    maxy = pointsG[0][1]

    for pxy in pointsG:
        if pxy[1] < miny:
            miny = pxy[1]
        if pxy[1] > maxy:
            maxy = pxy[1]
    # print(maxy - miny)
    if (maxy - miny > 200):
        print("JUMP")
	#press('up')
        pointsG.clear()
>>>>>>> 3759948ee7ff67740e18ddc1106a1d901fd91e72
    # print(contour)
    # print(points)


    output = cv2.bitwise_and(frame, frame, mask = maskG)
    output2 = cv2.bitwise_and(frame, frame, mask = maskR)
    output = cv2.add(output , output2)

    cv2.circle(output, (int(centxG), int(centyG)), 10, (0,0,255), -1)
    cv2.circle(output, (int(centxR), int(centyR)), 10, (0, 255, ), -1)

    # show the images
    cv2.imshow("images", np.hstack([frame, output]))
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

if not args.get("video", False):
	vs.stop()
else:
	vs.release()
<<<<<<< HEAD



=======
 
>>>>>>> 3759948ee7ff67740e18ddc1106a1d901fd91e72
# close all windows
cv2.destroyAllWindows()
