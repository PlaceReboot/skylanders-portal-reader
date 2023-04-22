# skylanders-portal-reader
Simple Python code that interfaces with the Xbox 360 skylanders portal. So far I've only tested on the first portal, don't know about the rest.

What does this do? 
Well it awakens portal and then adds a custom color transition to it.
Pulsates red if there are no skylanders.
Blue if a skylander is added onto the base.
Waving green if the skylander stays on the base
Red if a skylander is fully removed from the base.

There are some unnecessary waits in it for showcase of what it was before and what it is after.
PS. I'm not that good with python but certainly better than with C++

# Requirements
pyusb
libusb
portal
skylander
zadig

# Instructions
First you must use zadig to convert the portal's usb drivers to WinUSB, this is apparently irreversible (when i tried it really did just replace the driver).
Second you must install libusb.
Third pip install pyusb.
Lastly, run the code (might need to run as admin).

# Notes
Note that to modify it you will require their RFID protocol:
https://github.com/tresni/PoweredPortals/wiki/USB-Protocols <- my savior, without this repo the entire project would never exist!!!
https://pastebin.com/EqtTRzeF
