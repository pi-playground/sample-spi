# !	/user/bin/env python
import time
file_abs = "/dev/spidev0.0"
f  =  open(file_abs, "rw")

f.write("\xFF");
time.sleep(3)
f.write("\x00");
time.sleep(3)


f.write("\xFF");
time.sleep(3)
f.write("\x00");
time.sleep(3)


f.write("\xFF");
time.sleep(3)
f.write("\x00");
time.sleep(3)


f.write("\xFF");
time.sleep(3)
f.write("\x00");
time.sleep(3)

