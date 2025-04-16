import pywhatkit
import flask
import pyautogui
import socket
import qrcode
from io import BytesIO
import PIL.Image


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


default_port = 8000


server_url = f"http://{local_ip}:{default_port}"



qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10, 
    border=4,  
)
qr.add_data(server_url)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")


img.show() 


pywhatkit.start_server(port=default_port)
