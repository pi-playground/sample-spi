# !	/user/bin/env python
import time
file_abs = "/dev/spidev0.0"
f  =  open(file_abs, "w")

f.write("\x00\n");
time.sleep(3)
f.write("\xFF\n");
time.sleep(3)


f.write("\xFF\n");
time.sleep(3)
f.write("\x00\n");
time.sleep(3)


f.write("\xFF\n");
time.sleep(3)
f.write("\x00\n");
time.sleep(3)


f.write("\xFF\n");
time.sleep(3)
f.write("\x00\n");
time.sleep(3)

