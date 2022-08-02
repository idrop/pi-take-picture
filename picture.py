#!//usr/bin/python3

import time
from pathlib import Path

from picamera2 import Picamera2


def take_pic():
    picam2 = Picamera2()
    config = picam2.create_still_configuration()
    picam2.configure(config)
    picam2.start()
    time.sleep(5)
    now = time.strftime("%Y%m%d-%H%M%S", time.gmtime())
    np_array = picam2.capture_array()
    print(np_array)

    home_dir = str(Path.home())
    picam2.capture_file(home_dir + "/current/" + now + ".jpg")
    picam2.stop()


take_pic()
