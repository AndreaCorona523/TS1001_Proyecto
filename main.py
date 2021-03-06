import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage
import cv2
import librerias_kernel as lbk
import argparse

#Funcion para agregar padding
def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
    
def procesamiento_imagen(imagen):
    Is = Image.open(imagen); #Imagen del perro
    I = Is.convert('L'); #Convierte imagen a escala de grises
    I = numpy.asarray(I); #Conversion numerica para operar de 0-1
    I = I / 255.0; #Normalizacion 0-1

    #Se agrega padding
    I = numpy.pad(I, 10, pad_with, padder=0)

    #Kernel Sombrero
    ks=lbk.kernel_sombrero(3,15)

    #Kernel Gauss
    kg=lbk.gauss(10,15)

    #Kernel Laplacian
    klp = lbk.laplacianOfGaussian(5,15)

    #Se aplica Kernel Sombrero a Imagen
    Imagen = ndimage.convolve(I, ks, mode='constant', cval=0.0)

    #Se aplica Kernel Gauss a Imagen
    Imagen1 = ndimage.convolve(I, kg, mode='constant', cval=0.0)

    #Se aplica Laplacian a Imagen
    Imagen2 = ndimage.convolve(I, klp, mode='constant', cval=0.0)

    #Se aplica Kernel sepia a Imagen
    Imagen3 = lbk.sepia(imagen);

    #Se ajusta tamaño de Figura
    plt.figure(figsize = (15,15))

    #Imagen original 
    plt.subplot(3,3,1)
    plt.imshow(Is)
    plt.xlabel('Input Image')

    #Imagen con kernel Sombrero
    plt.subplot(3,3,2)
    plt.imshow(Imagen)
    plt.xlabel('Kernel Sombrero sigma=3')

    #Imagen con kernel Gauss
    plt.subplot(3,3,3)
    plt.imshow(Imagen1)
    plt.xlabel('Kernel Gauss sigma = 10')

    #Imagen con kernel Laplacian
    plt.subplot(3,3,7)
    plt.imshow(Imagen2)
    plt.xlabel('Kernel Laplacian sigma= 5')

    #Imagenes con kernel Sepia
    plt.subplot(3,3,8)
    plt.imshow(Imagen3)
    plt.xlabel('Kernel Sepia')
    
    plt.grid(False)
    
 #mostrar imagenes    
    plt.show()

if __name__ == "__main__":
    #get image arguments from the shell  "python main.py Sample.png"
    ap = argparse.ArgumentParser()
    ap.add_argument("image", help="Path to the image", type=str)
    args = ap.parse_args()
    procesamiento_imagen(args.image)

