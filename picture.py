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
    gmtime = time.gmtime()
    today = time.strftime("%Y%m%d", gmtime)
    timeToday = time.strftime("%H%M%S", gmtime)
    np_array = picam2.capture_array()
    print(np_array)

    picam2.capture_file(str(Path.home()) + "/captures/" + today + "/" + timeToday + ".jpg")
    picam2.stop()

take_pic()
