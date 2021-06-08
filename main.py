import cv2
import numpy as np
circles=np.zeros((4,2),np.int)
counter=0
img = cv2.imread('kings.jpeg')
def mousePoints(event, x, y, flags, params):
   global counter
   if event == cv2.EVENT_LBUTTONDOWN:
       circles[counter]=x,y
       counter+=1
       print(circles)

while True:
  if counter==4:
        width, height = 250, 350
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        out = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow('image', out)

  for x in range(0,4):
    cv2.circle(img, circles[x], 5, (0, 0, 255), cv2.FILLED)
  cv2.imshow('img', img)
  cv2.setMouseCallback('img', mousePoints)

  cv2.waitKey(1)


