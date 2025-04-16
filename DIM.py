import requests
from bs4 import BeautifulSoup
import os

url = 'https://pin.it/3cjCaLicI'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
images = soup.find_all('img')


for image in images:
    url = image['src']
    name = image['alt']

    gim = requests.get(url)

    if gim.status_code == 200:
        spath = r'C:\Users\57314\Desktop\Scripts_Piolas\web_img'
        full_path = os.path.join(spath, name + '.jpg')
        with open(full_path, 'wb') as f:
            f.write(gim.content)
    else:
        print('Error al descargar la imagen')
        
        


