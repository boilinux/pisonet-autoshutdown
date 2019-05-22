import usb.core
import usb.util
import os
import time

device_id_vendor=0x413C #Update to your keyboard Id Vendor
device_id_product=0x2110 #Update to your keyboard Id Product
dev = 0

def check_device():
    global device_id_vendor
    global device_id_product
    global dev
    
    dev = usb.core.find(idVendor=device_id_vendor, idProduct=device_id_product)

while 1:
    check_device()

    # was it found?
    if dev is None:

	time.sleep(60)
	check_device()
	if dev is None:
            # not found
            os.system('shutdown -s -f -t 20') 
            while 1:
                check_device()
                if dev is not None:
                    os.system('shutdown /a')
                    break
                
                time.sleep(1)

    time.sleep(10)
