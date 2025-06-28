#zoop
import ugit
import gc
import utime
import micropython

from vga_driver import TinyVgaDriver

from ir_rx.nec import NEC_8

def ir_callback(data, addr, ctrl):
    if data < 0:
        pass
    else:
        print(data)

ir = NEC_8(1, ir_callback)



vga = TinyVgaDriver(debug=True)
print(micropython.mem_info())
vga.start_synchronisation()
print(micropython.mem_info())
utime.sleep_ms(1000)


running = True
try:
    while running:
        vga.fbuf.line(0, 120, 320, 121, vga.COLOR_RED)
        
        vga.fbuf.line(0, 0, 320, 240, vga.COLOR_RED)
       
except KeyboardInterrupt:
    vga.stop_synchronisation()

