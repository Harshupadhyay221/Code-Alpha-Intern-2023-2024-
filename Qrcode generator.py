import qrcode as qr #  qr code is a module in python which help to built qrcodes#
url = input("Enter the URL: ")
img = qr.make(url)
img.save("linkdin.png")


