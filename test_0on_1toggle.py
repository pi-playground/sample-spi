import spidev
import time
from  gpiozero import DigitalOutputDevice
switch =  DigitalOutputDevice(12, initial_value=0)
switch.off()

def latchData():
	switch.on()
	time.sleep(0.001)
	switch.off()

spi = spidev.SpiDev()
spi.open(0, 0)
spi.writebytes([0x00,0x00])
latchData()
time.sleep(3)
spi.writebytes([0xff,0x00])
latchData()
time.sleep(3)
spi.writebytes([0x00,0x00])
latchData()
time.sleep(3)
spi.writebytes([0xff,0x00])
latchData()
time.sleep(3)
spi.close()