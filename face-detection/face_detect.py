import cv2
import sys
# parametros

imagePath = sys.argv[1]
cascPath = sys.argv[2]

#criar a cascade
faceCascade = cv2.CascadeClassifier(cascPath)

#lendo a imagem
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#detectar a face na imagem

faces = faceCascade.detectMultiScale(
	gray,
	scaleFactor=1.1,
	minNeighbors = 5,
	minSize = (30,30),
	flags =  cv2.cv.CV_HAAR_SCALE_IMAGE
)

#retorno da funcao e uma lista de retangulos que serao as possiveis faces detectadas

print "Found {0} faces!".format(len(faces))

#desenhar o retangulo em volta da imagem
for(x, y, w, h) in faces:
	cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)


#gera o retangulo desenhado
cv2.imshow("Faces encontradas", image)
cv2.waitKey(0)

