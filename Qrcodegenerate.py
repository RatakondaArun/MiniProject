import qrcode
# qr=qrcode.make(" creating mrv technology")
# data="https://mrvtechnology.com/ "
# qr=qrcode.make(data)
# qr.save(" mrvqr1.png")

qr=qrcode.QRCode(
    version=5,
    box_size=5,
    border=3
)
Name=input("enter ur name:")
age=input("enter ur age:")
email=input("enter ur email:")
phone_number=input("enter ur Phone_number:")
Data={"Name":Name,"Age": age,"Email":email,"Phone_number":phone_number}
qr.add_data(Data)
qr.make(fit=True)
img=qr.make_image()
img.save("Store_details_in_qr3.png")
