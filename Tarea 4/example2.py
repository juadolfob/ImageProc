import cv2 as cv

img = cv.imread('./resources/img.pgm')

cv.imwrite("identidad.jpg", img)


def inverte(imagem, name):
    imagem = (255-imagem)
    cv.imwrite(name, imagem)


inverte(img, "invertido.jpg")

ret, img_binary = cv.threshold(img, 40, 255, cv.THRESH_BINARY)
cv.imwrite('umbral.jpg',img_binary)

inverte(img_binary,'umbral_invert.jpg')
