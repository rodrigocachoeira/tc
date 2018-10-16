import os
import sys
import shutil
from os import listdir
from PIL import Image
from os.path import isfile, join

class Images:

    #Diretório que contém todas as imagens
    path = './all/'

    #Diretório que irá armazenar individualmente por pastas
    #as cópias das imagens
    segmented_path = './xrays/'

    #Ajusta a largura padrão que todas
    #as imagens devem ter
    default_width = 3000

    #Ajusta a altura padrão que todas
    #as imagens devem ter
    default_height = 1200

    #Tamanho que cada parte de imagem
    #deve possuir
    part_image = 500

    #Verfica se um diretório está vazio
    def dir_empty(self):
        return len(os.listdir(self.segmented_path)) == 0

    #Realiza uma cópia das imagens para uma pasta
    #individual
    def copy_images(self, files):
        for n, xray in enumerate(files):
            xray_folder = Images.segmented_path + str(n)
            if not os.path.exists(xray_folder):
                os.makedirs(xray_folder)
            shutil.copy(Images.path + xray, xray_folder + "/original.png")

    #Ajusta a imagem para um tamanho
    #padrão
    def resize_images(self):
        for folder in listdir(Images.segmented_path):
            xray_folder = Images.segmented_path + "/" + folder
            xray = xray_folder + "/original.png"

            with Image.open(xray) as image:
                new_file = image.resize((Images.default_width, Images.default_height))
                new_file.save(xray_folder + "/xray.png")

                print("file {} resized".format(new_file))