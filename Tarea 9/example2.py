import cv2
import numpy as np
import matplotlib.pyplot as plt

def connected_component_label(path):

    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fig, ax = plt.subplots(1, figsize=(12, 8))
    plt.title("Original")
    plt.imshow(image)

    Gx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    Gy = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

    img_Gx = cv2.filter2D(image, -1, Gx)
    fig, ax = plt.subplots(1, figsize=(12, 8))
    plt.title("Gx kernel")
    plt.imshow(img_Gx)

    img_Gy = cv2.filter2D(image, -1, Gy)
    fig, ax = plt.subplots(1, figsize=(12, 8))
    plt.title("Gy kernel")
    plt.imshow(img_Gy)

    imgg=img_Gy+img_Gx
    fig, ax = plt.subplots(1, figsize=(12, 8))
    plt.title("G kernel")
    plt.imshow(imgg)

    plt.show()

connected_component_label('img2.jpg')