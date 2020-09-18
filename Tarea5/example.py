import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('pp.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.jpg', gray)

plt.hist(image.ravel(), 256, [0, 256]);
plt.show()

image = cv2.imread('pp.png', cv2.IMREAD_GRAYSCALE)
cv2.equalizeHist(image)
cv2.imshow('Histogram', image)

plt.hist(image.ravel(), 256, [0, 256]);
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


img = cv2.imread('pp.png')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()