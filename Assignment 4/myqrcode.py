import qrcode

name = (input("entar your number: "))
phone = int(input("enter your phone: "))

qrcode = qrcode.make(name + "\n" + str(phone))
qrcode.save("my name and phone.png")
