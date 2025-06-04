import qrcode

target_url = input("Please enter the URL you want to convert into a QR code, e.g., your LinkedIn URL: ")

qr = qrcode.QRCode(
  version = 3,
  box_size = 20,
  border = 10,
  error_correction = qrcode.constants.ERROR_CORRECT_H
)

qr.add_data(target_url)
qr.make(fit = True)

qr_image = qr.make_image(fill_color = "black", back_color="white")

qr_image.save('MyQRCode.png', format = 'PNG')
