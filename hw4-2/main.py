import pyb, sensor, image, time, math
import sensor, image, time
enable_lens_corr = False # turn on for straighter lines...
sensor.reset()
sensor.set_pixformat(sensor.RGB565) # grayscale is faster
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()
# All lines also have x1(), y1(), x2(), and y2() methods to get their end-points
# and a line() method to get all the above as one 4 value tuple for draw_line().

uart = pyb.UART(3,9600,timeout_char=1000)
uart.init(9600,bits=8,parity = None, stop=1, timeout_char=1000)

while(True):
   count=0
   d=[]
   output=0

   clock.tick()
   img = sensor.snapshot()
   if enable_lens_corr: img.lens_corr(1.8) # for 2.8mm lens...

   # merge_distance controls the merging of nearby lines. At 0 (the default), no
   # merging is done. At 1, any line 1 pixel away from another is merged... and so
   # on as you increase this value. You may wish to merge lines as line segment
   # detection produces a lot of line segment results.

   # max_theta_diff controls the maximum amount of rotation difference between
   # any two lines about to be merged. The default setting allows for 15 degrees.

   for l in img.find_line_segments(merge_distance = 0, max_theta_diff = 5):
      if (l[6]>160 or l[6]<20) and 50<l[0] and 50<l[2] and l[0]<130 and l[2]<130:
        img.draw_line(l.line(), color = (255, 0, 0))
        if(l[6]<20):
            d.append(l[6]+180)
        if(l[6]>160):
            d.append(l[6])
        count=count+1
   for it in range(0,count):
        output=output+d[it]
   if count!=0:
    output=output/count


    print(output)
    uart.write(("%f\r\n"% output).encode())

    #print("FPS %f" % clock.fps())
    time.sleep(0.5)