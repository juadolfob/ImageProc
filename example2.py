import cv2
import numpy as np
import matplotlib.pyplot as plt

def connected_component_label(path):
    image = cv2.imread(path)
    plt.title("Original")
    plt.imshow(image)
    image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fig, ax = plt.subplots(1, figsize=(12, 8))
    plt.title("BLACK AND WHITE")
    plt.imshow(image)

    #Sobel creo
    sobel_gx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    sobel_gy = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    imgg = cv2.filter2D(image[:],-1,sobel_gx)
    imgg = cv2.filter2D(imgg,-1,sobel_gy)
    fig, ax = plt.subplots(1, figsize=(12, 8))
    plt.title("Sobel")
    plt.imshow(imgg)

    #Prewit
    prewit_gx = np.array([[1,0,-1], [1,0,-1], [1,0,-1]])
    prewit_gy = np.array([[1,1,1], [0,0,0], [-1,-1,-1]])
    imgg = cv2.filter2D(image[:], -1, prewit_gx)
    imgg = cv2.filter2D(imgg, -1, prewit_gy)
    fig, ax = plt.subplots(1, figsize=(12, 8))
    plt.title("Prewit")
    plt.imshow(imgg)

    # Roberts
    roberts_gx = np.array([[1, 0],[0,-1]])
    roberts_gy = np.array([[0,1],[-1,0]])
    imgg = cv2.filter2D(image[:], -1, roberts_gx)
    imgg = cv2.filter2D(imgg, -1, roberts_gy)
    fig, ax = plt.subplots(1, figsize=(12, 8))
    plt.title("Roberts")
    plt.imshow(imgg)

    # Canny
    imgg = cv2.Canny(image[:], 100, 200)
    fig, ax = plt.subplots(1, figsize=(12, 8))
    plt.title("Canny")
    plt.imshow(imgg)
    plt.show()

    #Erosión
    kernel = np.ones((7, 7), np.uint8)
    imgg = cv2.erode(image[:], kernel, iterations=1)
    plt.title("erosion")
    plt.imshow(imgg)
    plt.show()

    #Dilatación
    imgg = cv2.dilate(image[:],kernel,iterations = 1)
    plt.title("Dilatación")
    plt.imshow(imgg)
    plt.show()

    # MORPH_OPEN
    imgg = cv2.morphologyEx(image[:], cv2.MORPH_OPEN, kernel)
    plt.title("MORPH_OPEN")
    plt.imshow(imgg)
    plt.show()

    # MORPH_CLOSE
    imgg = cv2.morphologyEx(image[:], cv2.MORPH_CLOSE, kernel)
    plt.title("MORPH_CLOSE")
    plt.imshow(imgg)
    plt.show()

    # MORPH_GRADIENT
    imgg = cv2.morphologyEx(image[:], cv2.MORPH_GRADIENT, kernel)
    plt.title("MORPH_GRADIENT")
    plt.imshow(imgg)
    plt.show()

#connected_component_label('camino.jpg')

cap = cv2.VideoCapture('test.mp4')

# Define the codec and create VideoWriter object
fourcc =  cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4',0x7634706d , 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is not True:
        break
    imgg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((7, 7), np.uint8)

    # MORPH_CLOSE
    imgg = cv2.morphologyEx(imgg, cv2.MORPH_CLOSE, kernel)

    imgg = cv2.erode(imgg, kernel, iterations=1)

    # Dilatación
    imgg = cv2.dilate(imgg, kernel, iterations=1)

    roberts_gx = np.array([[1, 0], [0, -1]])
    roberts_gy = np.array([[0, 1], [-1, 0]])
    imgg = cv2.filter2D(imgg, -1, roberts_gx)
    imgg = cv2.filter2D(imgg, -1, roberts_gy)

    out.write(imgg)
    cv2.imshow('frame',imgg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()