
from machine import Pin

from ir_rx.print_error import print_error
from ir_rx.nec import NEC_8

import ugit
import gc
import utime
import micropython
from vga_driver import TinyVgaDriver

pin_ir = Pin(28, Pin.IN)

def decodeKeyValue(data):
    if data == 0x16:
        return "0"
    if data == 0x0C:
        return "1"
    if data == 0x18:
        return "2"
    if data == 0x5E:
        return "3"
    if data == 0x08:
        return "4"
    if data == 0x1C:
        return "5"
    if data == 0x5A:
        return "6"
    if data == 0x42:
        return "7"
    if data == 0x52:
        return "8"
    if data == 0x4A:
        return "9"
    if data == 0x09:
        return "+"
    if data == 0x15:
        return "-"
    if data == 0x7:
        return "EQ"
    if data == 0x0D:
        return "U/SD"
    if data == 0x19:
        return "CYCLE"
    if data == 0x44:
        return "PLAY/PAUSE"
    if data == 0x43:
        return "FORWARD"
    if data == 0x40:
        return "BACKWARD"
    if data == 0x45:
        return "POWER"
    if data == 0x47:
        return "MUTE"
    if data == 0x46:
        return "MODE"
    return "ERROR"

def ir_callback(data, addr, ctrl):
    if data < 0:
        pass
    else:
        print(decodeKeyValue(data))

ir = NEC_8(pin_ir, ir_callback)
ir.error_function(print_error)


vga = TinyVgaDriver(debug=True)
print(micropython.mem_info())
vga.start_synchronisation()
print(micropython.mem_info())


running = True
try:
    while running:
        vga.fbuf.line(0, 120, 320, 121, vga.COLOR_RED)
        
        vga.fbuf.line(0, 0, 320, 240, vga.COLOR_RED)
       
except KeyboardInterrupt:
    ir.close()
    vga.stop_synchronisation()


