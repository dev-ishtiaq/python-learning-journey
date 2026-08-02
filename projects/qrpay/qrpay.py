import qrcode

upi_id = input("Enter your UPI ID = ")

bkash_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
rocket_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
nagad_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


bkash_qr = qrcode.make(bkash_url)
rocket_qr = qrcode.make(rocket_url)
nagad_qr = qrcode.make(nagad_url)


bkash_qr.save('bkash_qr.png')
rocket_qr.save('rocket_qr.png')
nagad_qr.save('nagad_qr.png')


bkash_qr.show()
rocket_qr.show()
nagad_qr.show()