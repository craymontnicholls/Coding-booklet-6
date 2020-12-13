
import random
import time


def eye_catching(start, end):
  percent = start
  print("{}% off".format(percent))


  while percent < end:
    percent += random.randint(1,20)
    if percent > end:
      temp_val = percent - end
      percent = percent - temp_val


    print("{}% off".format(percent))
    time.sleep(0.5)


eye_catching(10,60)