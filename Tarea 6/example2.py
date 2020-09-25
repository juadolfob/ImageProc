import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image 
image = cv2.imread('img.png')


# Apply log transformation method 
c = 255 / np.log(1 + np.max(image))

log_image = image.copy()
for channel in range(log_image.shape[2]):
    for x in range(log_image.shape[0]):
        for y in range(log_image.shape[1]):
            log_image.itemset((x, y, channel), c * (np.log(log_image.item(x, y, channel) + 1)))
# Specify the data type so that 
# float value will be converted to int 
log_image = np.array(log_image, dtype=np.uint8)

cv2.imshow("Images", np.hstack([image, log_image]))
cv2.waitKey(0)