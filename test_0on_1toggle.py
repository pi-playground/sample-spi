import spidev
import time
from  gpiozero import DigitalOutputDevice
root_power =  DigitalOutputDevice(21, initial_value=0, active_high=False)
switch =  DigitalOutputDevice(12, initial_value=0)
oe =  DigitalOutputDevice(16, initial_value=0)
oe.off()
switch.off()
root_power.on()


def latchData():
	switch.on()
	time.sleep(0.001)
	switch.off()

spi = spidev.SpiDev()
spi.max_speed_hz = 5000
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