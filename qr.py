import qrcode
from dotenv import load_dotenv
import os
load_dotenv()

image = qrcode.make(os.getenv("RESTAURANT_URL"))
image.save("qr_code.png")