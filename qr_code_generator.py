#__author__ = Vikas Mangal(kawachh)
import qrcode
from PIL import Image, ImageDraw, ImageFont
data = ["Vikas", "Mangal"] #List of strings which we want to convert in qr codes

for code in data:
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=5)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image()
    w,h = img.size
    font = ImageFont.truetype('font.ttf', size=24)
    color = 'rgb(0, 0, 0)'
    draw = ImageDraw.Draw(img)
    text_w, text_h = draw.textsize(code, font)
    text_h += 15
    draw.text(((w-text_w) // 2, h - text_h), code, fill = color, font = font)
    draw.text(((w-text_w) // 2, h - text_h), code, fill = color, font = font)
    img.save("qr_codes/" + code+".jpg")




