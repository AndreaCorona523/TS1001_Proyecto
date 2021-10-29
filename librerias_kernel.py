import numpy
import cv2
 
#Funcion para el Kernel del sombrero 
#Parametros iniciales valor de sigma y tamaño de matriz (k)
def kernel_sombrero(sigma,k): 
    matrix=numpy.zeros((k,k));  #Crear matriz de K x K con valor 0
  # For para recorer todos los valores en eje horizontal y vertical 
    for x in range (0,k):  
        for y in range (0,k): 
            #Formula para el filtro del sombrero en 2D
            matrix[x][y]=1/(numpy.pi*sigma**4)*(1-1/2*(x**2+y**2)/sigma**2) \
                         * numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return matrix #Regresamos la matriz con el filtro 
   
#Funcion para el Kernel de Guass 
#Parametros iniciales valor de sigma y tamaño de matriz (k)   
def gauss(sigma,k):
    g=numpy.zeros((k,k)); #Crear matriz de K x K con valor 0
   # For para recorer todos los valores en eje horizontal y vertical 
    for x in range (0,k):
        for y in range (0,k):
            g[x][y]=1/(2*numpy.pi*sigma**2)*numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return g #Regresamos la matriz con el filtro 
   
   
#Aquí se tiene el segmento utilizado para el filtro laplaciano que ocupa antes
#un filtro Gaussiano para su proceso

def laplacianOfGaussian(sigma, K):
    Matrix = numpy.zeros((K,K))
    for x in range(0,K):
        for y in range(0,K):
            Matrix[x][y] = -(1/(numpy.pi*sigma**4)) * (1-((x**2+y**2)/(2*sigma**2))) \
                        * numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return Matrix #Regresamos la matriz con el filtro 

def sepia(imagen):
  img = cv2.imread(imagen)
  original = img.copy()
  img = cv2.transform(img, numpy.matrix([[0.272, 0.534, 0.131],
                                      [0.349, 0.686, 0.168],
                                      [0.393, 0.769, 0.189]])) # Imagen*matriz sepia 
  img[numpy.where(img > 255)] = 255 # normalizando valores mayores que 255 
  return img #Regresamos la matriz con el filtro 
