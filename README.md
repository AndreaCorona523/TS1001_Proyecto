# TS1001_Proyecto
Este es el directorio para el proyecto final de la materia TS1001
# Funcionamiento
Este proyecto realiza una aplicación de kernel en la imagen a través de convoluciones. En este caso se requieren 2 archivos: librerias_Kernel.py el cual cuenta con las funciones para obtener los kernels y el main.py que es donde llamamos a todas las funciones y aplicamos los filtros a la imagen, además es la encargada de llevar a cabo las convoluciones y mostrar la imagen con los filtros.

# Kernels implementados 
## Sombrero mexicano 
Es la segunda derivada normalizada negativa de una función gaussiana,este tipo de filtros de diferencia (que tienen coeficientes positivos y negativos) el efecto es el contrario, donde las diferencias entre niveles de intensidad de pixel son realzadas. Por consiguiente, este tipo de filtros son utilizados normalmente para el realce de bordes, para su detección, como el caso de frecuencia para modelar datos sísmicos.[1] 

## Gauss Blur
El desenfoque gaussiano es un tipo de filtro de desenfoque de imagen que utiliza una función gaussiana para calcular la transformación que se aplicará a cada píxel de la imagen. Es utilizado en software de gráficos, generalmente para reducir el ruido de la imagen y reducir los detalles. [2]

## Laplaciano 
El laplaciano es una medida isotrópica bidimensional de la segunda derivada espacial de una imagen. El laplaciano de una imagen resalta las regiones de cambio rápido de intensidad y, por lo tanto, se utiliza a menudo para la detección de bordes. Este filtro se aplica a menudo a una imagen que primero se ha suavizado con algo que se aproxima a un filtro de suavizado gaussiano para reducir su sensibilidad al ruido.[3]

## Sepia
El efecto sepia le da a sus imágenes un tono marrón cálido. El filtro sepia mejora el aspecto general de su imagen. Es un procedimiento que consiste en sustituir los grises de una fotografía en blanco y negro por una tonalidad sepia el cual es un color marron oscuro y de saturación débil.[4][https://medium.com/dataseries/designing-image-filters-using-opencv-like-abode-photoshop-express-part-2-4479f99fb35]
# Bibliografias 
1)https://en.wikipedia.org/wiki/Ricker_wavelet
2)https://en.wikipedia.org/wiki/Gaussian_blur
3)https://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm
4)https://medium.com/dataseries/designing-image-filters-using-opencv-like-abode-photoshop-express-part-2-4479f99fb35
