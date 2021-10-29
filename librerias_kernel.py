import numpy
 
#Funcion para el Kernel del sombrero 
#Parametros iniciales valor de sigma y tamaño de matriz (k)
def kernel_sombrero(sigma,k):
    matrix=numpy.zeros((k,k)); #Crear matriz de K x K con valor 0
    for x in range (0,k): # For para recorer todos los valores en eje horizontal
        for y in range (0,k): #For para recorer todos los valores en eje vertical
      #Formula para el filtro del sombrero en 2D
            matrix[x][y]=1/(numpy.pi*sigma**4)*(1-1/2*(x**2+y**2)/sigma**2)
            matrix[x][y]= matrix[x][y] * numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return matrix #Regresamos la matriz con el filtro 

#Funcion para el Kernel de Gauss
#Parametros iniciales valor de sigma y tamaño de matriz (k)
def gauss(sigma,k):
    g=numpy.zeros((k,k)); #Crear matriz de K x K con valor 0
    for x in range (0,k): # For para recorer todos los valores en eje horizontal
        for y in range (0,k): #For para recorer todos los valores en eje vertical
      #Formula para el filtro de Gauss en 2D
            g[x][y]=1/(2*numpy.pi*sigma**2)*numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return g #Regresamos la matriz con el filtro
   
   
#Aquí se tiene el segmento utilizado para el filtro laplaciano que ocupa antes
#un filtro Gaussiano para su proceso

def LoG(sigma, x, y):
    laplace = -1/(numpy.pi*sigma**4)(1-(x**2+y**2)/(2*sigma**2))*numpy.exp(-(x**2+y**2)/(2*sigma**2))
    return laplace

def LoG_discrete(sigma, n):
    l = numpy.zeros((n,n))
    for i in range(n):
        for j in range(n):
            l[i,j] = LoG(sigma, (i-(n-1)/2),(j-(n-1)/2))
    return l
