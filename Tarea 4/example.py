import cv2

image = cv2.imread('img.png')

# rgb a grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)


# negativo

def inverte(imagem, name):
    imagem = (255-imagem)
    cv2.imwrite(name, imagem)

inverte(image, "invertido.jpg")

# umbral

ret, img_binary = cv2.threshold(image, 40, 255, cv2.THRESH_BINARY)
cv2.imwrite('umbral.jpg',img_binary)

inverte(img_binary,'umbral_invert.jpg')


# channel split

b,g,r = cv2.split(image)

cv2.imshow('b',b)
cv2.imshow('g', g)
cv2.imshow('r', r)


cv2.waitKey(0)
cv2.destroyAllWindows()