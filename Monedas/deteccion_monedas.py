import cv2 as cv
import numpy as np

imagen = cv.imread('vision_proyecto/mon4.JPG',0)
img = cv.GaussianBlur(imagen,(5,5),5)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1.0131,20)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
	cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
	cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
	if (i[2] <= 58):
		print("Moneda de 1 pesos, r =",i[2])
	elif (58 < i[2] <= 63):
		print("Moneda de 2 pesos, r =",i[2])
	elif(63 < i[2] < 69):
		print("Moneda de 5 pesos, r =",i[2])
	elif (69 <= i[2]):
		print("Moneda de 10 pesos, r =",i[2])
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()