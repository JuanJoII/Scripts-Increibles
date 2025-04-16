import os
import shutil

ruta_origen = r'D:\VHCC\Google_Fotos_VH'

ruta_destino_final = 'D:\MULTIMEDIA_ORGANIZADA'

nombre_carpeta_origen = os.path.basename(ruta_origen)

ruta_imagenes = os.path.join(ruta_origen, f'IMG_{nombre_carpeta_origen}')
ruta_videos = os.path.join(ruta_origen, f'VID_{nombre_carpeta_origen}')

os.makedirs(ruta_imagenes, exist_ok=True)
os.makedirs(ruta_videos, exist_ok=True)

extensiones_imagenes = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
extensiones_videos = {'.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv', '.3GP'}


for archivo in os.listdir(ruta_origen):
    ruta_completa = os.path.join(ruta_origen, archivo)
    
   
    if os.path.isfile(ruta_completa):
        
        nombre, extension = os.path.splitext(archivo)
        extension = extension.lower()
        

        if extension in extensiones_imagenes:
            shutil.move(ruta_completa, os.path.join(ruta_imagenes, archivo))
            print(f'Movido {archivo} a {ruta_imagenes}')
        elif extension in extensiones_videos:
            shutil.move(ruta_completa, os.path.join(ruta_videos, archivo))
            print(f'Movido {archivo} a {ruta_videos}')
        else:
            print(f'Archivo {archivo} no es una imagen ni un video, no se moverá.')


shutil.move(ruta_imagenes, ruta_destino_final)
shutil.move(ruta_videos, ruta_destino_final)

print(f'Organización completada. Carpetas movidas a {ruta_destino_final}.')