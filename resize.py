import os
from PIL import Image

def resize_images(directory, size):
    #Recorremos toda la carpeta y cogemos imágen por imagen
    for filename in os.listdir(directory):
        try:
            #comprogamos que el fichero sea una imágen 
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                #abrimos imágen, reescalamos y guardamos
                image = Image.open(os.path.join(directory, filename))
                #image.LANCZOS permite mejorar la calidad de imágen después de redimensionarla
                image = image.resize(size, Image.LANCZOS)
                image.save(os.path.join(directory, filename))
        except UnicodeEncodeError:
            print(f"No se puede editar la siguiente imágen: {filename}")

if __name__ == '__main__':
    width = 1920
    height = 1080
    directory = r"ruta"
    size = (width, height)
    resize_images(directory, size)
