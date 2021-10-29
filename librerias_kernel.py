import numpy
 
#Funcion para el Kernel del sombrero 
#Parametros iniciales valor de sigma y tamaño de matriz (k)
def kernel_sombrero(sigma,k):
    matrix=numpy.zeros((k,k)); #Crear matriz de K x K con valor 0
    for x in range (0,k): # For para recorer todos los valores en x 
        for y in range (0,k): #For para recorer todos los valores en y
      #Formula para el filtro del sombrero en 2D
            matrix[x][y]=1/(numpy.pi*sigma**4)*(1-1/2*(x**2+y**2)/sigma**2)
            matrix[x][y]= matrix[x][y] * numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return matrix #Regresamos la matriz con el filtro 

def gauss(sigma,k):
    g=numpy.zeros((k,k));
    for x in range (0,k):
        for y in range (0,k):
            g[x][y]=1/(2*numpy.pi*sigma**2)*numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return g
   
   
#Aquí se tiene el segmento utilizado para el filtro laplaciano que ocupa antes
#un filtro Gaussiano para su proceso

def LoG(sigma, x, y):
    laplace = -1/(numpy.pi*sigma**4)(1-(x**2+y**2)/(2*sigma**2))*numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return laplace

def LoG_discrete(sigma, k):
    l = numpy.zeros((k,k))
    for i in range(k):
        for j in range(k):
            l[i,j] = LoG(sigma, (i-(k-1)/2),(j-(k-1)/2))
    return l

sigma = 1.4

l = numpy.round(LoG_discrete(sigma, 9)*(-40/LoG(sigma,0,0)))
