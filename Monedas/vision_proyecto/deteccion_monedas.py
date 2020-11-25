#########################################
#	Materia: Vision Computacional 		#
#	Proyecto: Deteccion de Monedas		#
#		By: Rene Camacho 				#
#########################################

import cv #Importando modulo de Opencv 
import sys #Modulo para manipular los argumentos que se le dan al programa
import time #Calcular tiempo de proceso

tiempoi = time.time()

imagen = cv.LoadImage(sys.argv[1], cv.CV_LOAD_IMAGE_GRAYSCALE)
#Cargo la imagen (argv[1]) y le aplico el filtro de escala de grises

storage = cv.CreateMat(1, 8, cv.CV_32FC3)
#Creo la matriz en la que voy a meter los posibles circulos que sean encontrados en la imagen
#Si el numero de circulos es mayor que 8, el programa ya no funciona, deben de ser menor de 8

cv.Smooth(imagen, imagen, cv.CV_GAUSSIAN,5,5)
#Le aplico el filtro de Gaussian Blur y suavizo la imagen para eliminar el ruido

cv.HoughCircles(imagen, storage, cv.CV_HOUGH_GRADIENT, 1, 100)
#Aplico la funcion de "Hough Circles" para encontrar los circulos en la imagen

for n in range(0, storage.cols):
#El "Storage.cols" contiene el numero de circulos que fueron encontrados en la imagen
#For para diubjar los circulos que fueron encontrados en la imagen 
	r = cv.Get1D(storage, n)
	#Obtengo una tupla que contiene los valores del primer circulo que sea encontrado
	c = (cv.Round(r[0]), cv.Round(r[1]))
	#"c" es una tupla de dos valores redondeados del "cv.round" 
	#contiene la posicion del circulo
	cv.Circle(imagen, c, cv.Round(r[2]), cv.CV_RGB(0,0,0), 2)
	#Dibujo el circulo
	
	print r #Imprimiendo Tupla
	print r[2] #Imprimiendo radio de circulo
	
	#Con los radios encontrados, muestro que valor tiene la moneda
	if r[2] == 67.59068298339844:
		print "\nMoneda de $10 Detectada" 
	if r[2] == 68.31178283691406:
		print "\nMoneda de $5 Detectada"
	if r[2] == 60.84817123413086:
		print "\nMoneda de $2 Detectada"
	if r[2] == 52.50238037109375:
		print "\nMoneda de $1 Detectada"
	#Radios de 4 monedas juntas  
	if r[2] == 74.51509857177734:
		print "\nMoneda de $10 Detectada"
	if r[2] == 68.82223510742188:
		print "\nMoneda de $5 Detectada"
	if r[2] == 59.85398864746094:
		print "\nMoneda de $2 Detectada"
	if r[2] == 56.66127395629883:
		print "\nMoneda de $1 Detectada"
	#Radios de 4 monedas juntas, pero en fila
	if r[2] == 72.21149444580078:
		print "\nMoneda de $10 Detectada"
	if r[2] == 66.20045471191406:
		print "\nMoneda de $5 Detectada"
	if r[2] == 58.58753967285156:
		print "\nMoneda de $2 Detectada"
	if r[2] == 55.70008850097656:
		print "\nMoneda de $1 Detectada"

tiempof = time.time()
print "\nSe tardo: ",tiempof-tiempoi,"segundos" #Calculo Tiempo

print "\nHay un total de "+str(storage.cols)+" Moneda(s) detectada(s)." #Imprimo el total de monedas detectadas 
cv.NamedWindow("Deteccion de Monedas") #Ventana
cv.ShowImage("Deteccion de Monedas", imagen) #Muestro la Imagen
cv.WaitKey(0)