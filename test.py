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

check_device()

print(dev)
