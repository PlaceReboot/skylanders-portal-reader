import os
import usb
import time

device = usb.core.find(idVendor=0x1430, idProduct=0x1F17)
if device is None:
    raise ValueError('Portal not connected.')

device.set_configuration(1)
try:
    device.set_interface_altsetting(interface = 0, alternate_setting = 0)
except usb.USBError as e:
    print('not it chief')
    print(e)
    pass

message =  b'\x0B\x14\x52\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
response = device.write(0x2, message, 100)
print(response)
time.sleep(.1)
message = b'\x0B\x14\x41\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
response = device.write(0x2, message, 100)
time.sleep(1)
Color = 0xFF
Color2 = 0xFF
Alternating = -1
LastState = 0
while True:
    if device is None:
        raise ValueError('Portal not connected.')
    message = b'\x0B\x14\x53\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    device.write(0x2, message, 100)
    skylanders = device.read(0x81, len(message), 100)
    if LastState == skylanders[3]:
        if skylanders[3] == 0:
            message = b'\x0B\x14\x43'+ round(Color*.62).to_bytes(1, 'big') + b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            device.write(0x2, message, 100)
            Color -= 0x5
            if Color <= 0x0:
                Color = 0xFF
        else:
            message = b'\x0B\x14\x43\x00'+ Color2.to_bytes(1, 'big') +b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            device.write(0x2, message, 100)
            Color2 += (0x10*Alternating)
            if Color2 <= 0x40 or Color2 >= 0xFF:
                Alternating *= -1
    else:
        if skylanders[3] == 0:
            message = b'\x0B\x14\x43\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            device.write(0x2, message, 100)
            time.sleep(.5)
        else:
            message = b'\x0B\x14\x43\x00\x00\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            device.write(0x2, message, 100)
            time.sleep(.5)
    LastState = skylanders[3]
    time.sleep(.0005)
    
