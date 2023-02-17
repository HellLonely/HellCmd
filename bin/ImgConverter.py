import os
from PIL import Image
import bin.Deco as Deco


def start_module():
    Deco.image_converter()
    CargarImagen()

def CargarImagen():

    ruta_imagen = input("Pon la ruta de tu imagen. \n I -> ")
    image_format = input(" \n Formato de la imagen. (webp,jpg,png...) \n I -> ")

    im = Image.open(ruta_imagen)
    rgb_im = im.convert('RGB')

    split_image = ruta_imagen.split('.')


    ruta_conversion = split_image[0]
    print("\n El formato de la imagen es ."+ split_image[1])

    rgb_im.save(ruta_conversion+"-convert."+image_format, quality = 100)



# Diccionario de formatos escalables de imagenes

formart_dictionary = {
    '.png': 1,
    '.jpg': 2,
    '.jfif': 3,
    '.webp': 4
}

