#Generate QR code using python

import qrcode
data = "www.linkedin.com/in/usman-khan-735944353"
qr = qrcode.make(data)
qr.save("linkedin_qr.png")
print("QR code generated successfully!!")
print("QR code saved as linkedin_qr.png")