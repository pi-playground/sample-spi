import spidev
import time
spi = spidev.SpiDev()
spi.open(0, 0)
spi.writebytes([0x00,0xff])
time.sleep(3)
spi.writebytes([0xff,0xff])
time.sleep(3)
spi.writebytes([0x00,0x00])
time.sleep(3)
spi.writebytes([0xff,0x00])
time.sleep(3)

spi.open(0, 0)
spi.writebytes([0x00,0xff])
time.sleep(3)
spi.writebytes([0xff,0xff])
time.sleep(3)
spi.writebytes([0x00,0x00])
time.sleep(3)
spi.writebytes([0xff,0x00])
time.sleep(3)



spi.open(0, 0)
spi.writebytes([0x00,0xff])
time.sleep(3)
spi.writebytes([0xff,0xff])
time.sleep(3)
spi.writebytes([0x00,0x00])
time.sleep(3)
spi.writebytes([0xff,0x00])
time.sleep(3)

