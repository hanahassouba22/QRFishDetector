import pyzbar.pyzbar as pyzbar
from PIL import Image
import requests

img = input("QR image path: ")
decoded = pyzbar.decode(Image.open(img))
if decoded:
    url = decoded[0].data.decode('utf-8')
    if 'phish' in url.lower() or len(url) < 10:
        print("🚨 PHISHING RISK! Bad URL.")
    else:
        print("✅ SAFE QR!")
