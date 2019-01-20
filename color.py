# import the necessary packages
from pyautogui import press, keyDown, keyUp
import numpy as np
import cv2

from collections import deque
from imutils.video import VideoStream
import imutils
import time
import math

window_frame = 15
angle_thresh = 0.45
walk_thresh = 5
jump_thresh = 15

# Detector functions
<<<<<<< HEAD
def jump(pointsG, pointsR):
    if len(pointsG) == 0 and len(pointsR) == 0:
        return False
=======
def jump(pointsG , pointsR):
    
    if len(pointsG) == 0 and len(pointsR) == 0 :
        return False
    
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6
    if (len(pointsG) > 0):
        minyG = pointsG[0][1]
        maxyG = pointsG[0][1]

        for pxy in pointsG:
            if pxy[1] < minyG:
                minyG = pxy[1]
            if pxy[1] > maxyG:
                maxyG = pxy[1]

<<<<<<< HEAD
        if ((maxyG - minyG) > 175):
            print('Jump')
            return True

    if (len(pointsR) > 0):
=======
        for pxy in pointsG:
            if pxy[1] < minyG:
                minyG = pxy[1]
            if pxy[1] > maxyG:
                maxyG = pxy[1]

        if ((maxyG - minyG)> 175):
            print ('Jump')
            return True
 
    if(len(pointsR) > 0):
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6
        minyR = pointsR[0][1]
        maxyR = pointsR[0][1]
        for pxy in pointsR:
            if pxy[1] < minyR:
                minyR = pxy[1]
            if pxy[1] > maxyR:
                maxyR = pxy[1]
<<<<<<< HEAD

        if ((maxyR - minyR) > 175):
            print('Jump')
=======
    
     
        if ((maxyR - minyR)> 175):
            print ('Jump')
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6
            return True

    return False

def jump2(pointsG, pointsR):
    if (len(pointsG) < 2 or len(pointsR) < 2):
        return False
    elif ((pointsG[-1][1] - pointsG[-2][1]) > jump_thresh) and ((pointsR[-1][1] - pointsR[-2][1]) > jump_thresh):
        return True
    elif ((pointsG[-1][1] - pointsG[-2][1]) < -1*jump_thresh) and ((pointsR[-1][1] - pointsR[-2][1]) < -1* jump_thresh):
        return True
    else:
        return False

    

def get_dist(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2


def get_angle(point1, point2):
    return math.atan(1.0 * abs(point1[1] - point2[1]) / (abs(point1[0] - point2[0]) + 0.02))


# check if fingers are leaning for sideways motion
def lean(boxG, boxR):
<<<<<<< HEAD
    angle = -1
=======
    
    angleG = -1
    angleR = -1
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6

    if (len(boxG) == 0 and len(boxR) == 0):
        return False

<<<<<<< HEAD
    elif (len(boxG) > 0):
=======
    if (len(boxG) > 0):
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6
        len1 = get_dist(boxG[0], boxG[1])
        len2 = get_dist(boxG[1], boxG[2])

        if (len1 > len2):
<<<<<<< HEAD
            angle = get_angle(boxG[0], boxG[1])
        else:
            angle = get_angle(boxG[1], boxG[2])

    else:
=======
            angleG = get_angle(boxG[0], boxG[1])
        else:
            angleG = get_angle(boxG[1], boxG[2])
    
    if (len(boxR) > 0):
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6
        len1 = get_dist(boxR[0], boxR[1])
        len2 = get_dist(boxR[1], boxR[2])

        if (len1 > len2):
<<<<<<< HEAD
            angle = get_angle(boxR[0], boxR[1])
        else:
            angle = get_angle(boxR[1], boxR[2])

    if (angle == -1 or angle > 0.3):
        return False
    else:
        return True

=======
            angleR = get_angle(boxR[0], boxR[1])
        else:
            angleR = get_angle(boxR[1], boxR[2])

    if (angleG > angle_thresh and angleR > angle_thresh):
        return False
    else:
        return True
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6

# Check for walking requirements
def walk(pointsG, pointsR):
    new_color, high_color = "", ""
<<<<<<< HEAD
    if (len(pointsG) < 15 or len(pointsR) < 15):
        return False
=======
    if (len(pointsG) < window_frame or len(pointsR) < window_frame):
        return False
    
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6
    switch_count = 0
    if max(pointsG[-1*window_frame][0], pointsR[-1*window_frame][0]) == pointsG[-1*window_frame][0]:
        higher_colour = 'green'
    else:
        higher_colour = 'red'

<<<<<<< HEAD
    for value in range(-15, -1, 1):
=======
    for value in range(-1*window_frame,-1,1):
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6
        if max(pointsG[value][0], pointsR[value][0]) == pointsG[value][0]:
            new_colour = 'green'
        else:
            new_colour = 'red'

        if new_colour != higher_colour:
            switch_count += 1
            higher_colour = new_colour

    if switch_count > 2:
        return True
    else:
        return False


def walk2(pointsG, pointsR):
    if (len(pointsG) < 2 or len(pointsR) < 2):
        return False
    elif ((pointsG[-1][0] - pointsG[-2][0]) > walk_thresh) and ((pointsR[-1][0] - pointsR[-2][0]) < -1*walk_thresh):
        return True
    elif ((pointsG[-1][0] - pointsG[-2][0]) < -1*walk_thresh) and ((pointsR[-1][0] - pointsR[-2][0]) > walk_thresh):
        return True
    else:
        return False

# define the list of boundaries
boundaries = [
    ([89, 182, 0], [255, 255, 162])
]

boundariesLab = [
<<<<<<< HEAD
    ([0, 0, 0], [255, 120, 255]), ([0, 175, 0], [255, 255, 255])
=======
    ([ 0, 0, 0], [255, 120, 255]),([ 0, 175, 0], [255, 255, 255])
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6
]

vs = VideoStream(src=0).start()
time.sleep(2.0)

pointsG = []
pointsR = []

boxR = []
boxG = []

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    frame = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)


    # create NumPy arrays from the boundaries
    lowerG = np.array([0, 0, 0], dtype="uint8")
    upperG = np.array([255, 120, 255], dtype="uint8")

<<<<<<< HEAD
    lowerR = np.array([0, 163, 0], dtype="uint8")
    upperR = np.array([255, 255, 255], dtype="uint8")
=======
    lowerR = np.array([ 0, 163, 0], dtype = "uint8")
    upperR = np.array([255, 240, 255], dtype = "uint8")
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6

    # check if any contours more than threshold area
    foundG, foundR = False, False

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
<<<<<<< HEAD
    contoursG, h = cv2.findContours(maskG, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contoursR, h = cv2.findContours(maskR, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
=======
    _, contoursG, h = cv2.findContours(maskG ,cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    _, contoursR, h = cv2.findContours(maskR, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6

    for contour in contoursG:

        area = cv2.contourArea(contour)
<<<<<<< HEAD
        # print("rectangle")
        # print(rect)
        # print(area)
        if area > 2000:
            foundG = True
            M = cv2.moments(contour)
            if (len(pointsG) > 30):
                # print(pointsG)
=======
        if area > 2000:
            foundG = True
            M = cv2.moments(contour)
            if(len(pointsG) > 30):
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6
                pointsG.pop(0)
            pointsG.append((M['m10'] / M['m00'], M['m01'] / M['m00']))
            centxG = M['m10'] / M['m00']
            centyG = M['m01'] / M['m00']

            rect = cv2.minAreaRect(contour)
            boxG = cv2.boxPoints(rect)
            boxG = np.int0(boxG)
            cv2.drawContours(frame, [boxG], 0, (0, 0, 255), 2)

            break
    for contour in contoursR:

        area = cv2.contourArea(contour)
<<<<<<< HEAD
        # print(len(contour[0]))
        # print(area)
=======
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6
        if area > 2000:
            foundR = True
            M = cv2.moments(contour)
            if (len(pointsR) > 30):
                pointsR.pop(0)
            pointsR.append((M['m10'] / M['m00'], M['m01'] / M['m00']))
            centxR = M['m10'] / M['m00']
            centyR = M['m01'] / M['m00']

            rect = cv2.minAreaRect(contour)
            boxR = cv2.boxPoints(rect)
            boxR = np.int0(boxR)
            cv2.drawContours(frame, [boxR], 0, (0, 0, 255), 2)
<<<<<<< HEAD

            break

    if (not foundG):
        pointsG = []
    if (not foundR):
        pointsR = []

    # Check finger gesture

    if walk(pointsG, pointsR):
        print("walk")
        keyDown('right')
        keyUp('right')


    elif jump(pointsG, pointsR):
        pointsG = []
        pointsR = []
        keyDown('up')
        keyUp('up')
=======
        
            break

    if (not foundG and  len(pointsG)> 0):
        pointsG.pop()
    if (not foundR and  len(pointsR) > 0):
        pointsR.pop()

    # Check finger gesture

    if walk2(pointsG, pointsR) :
        print("walk")
        keyDown('right')
        keyUp('right')
        if(len(pointsG) > 15):
            pointsG = pointsG[15:]
        if(len(pointsR) > 15):
            pointsR = pointsR[15:]


    elif jump2(pointsG , pointsR) :
        keyDown('up')
        keyDown('up')
        keyDown('right')
        keyUp('up')
        keyUp('right')
        print("jump")
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6

    elif lean(boxG, boxR):
        print("lean")
        keyDown('left')
<<<<<<< HEAD
        keyDown('left')
=======
        keyUp('left')
>>>>>>> 6d7406133837264949b809c46304d85ec01a43b6

    output = cv2.bitwise_and(frame, frame, mask=maskG)
    output2 = cv2.bitwise_and(frame, frame, mask=maskR)
    output = cv2.add(output, output2)

    cv2.circle(output, (int(centxG), int(centyG)), 10, (0, 0, 255), -1)
    cv2.circle(output, (int(centxR), int(centyR)), 10, (0, 255,), -1)

    # show the images
    cv2.imshow("images", np.hstack([frame, output]))
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

vs.release()

# close all windows
cv2.destroyAllWindows()
