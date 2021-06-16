import time
import serial
import sys,tty,termios
global x
global y
global d

x =int(input('x'))
y =int(input('y'))
d =input('direct')
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch



if len(sys.argv) < 1:
    print ("No port input")
s = serial.Serial(sys.argv[1])

while(1):
    if d=='west':
        s.write("/turn/run -200 0.91 \n".encode())
        time.sleep(x*0.04)
        s.write("/stop/run \n".encode())
        time.sleep(1)
        
        s.write("/turn/run -250 -0.19 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
        time.sleep(1)

        s.write("/turn/run -200 0.91 \n".encode())
        time.sleep(y*0.04)
        s.write("/stop/run \n".encode())
    elif d=='east':
        s.write("/turn/run -200 0.91 \n".encode())
        time.sleep(x*0.04)
        s.write("/stop/run \n".encode())
        time.sleep(1)
        
        s.write("/turn/run -250 0.14 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
        time.sleep(1)

        s.write("/turn/run -200 0.91 \n".encode())
        time.sleep(y*0.04)
        s.write("/stop/run \n".encode())
    elif d=='south':
        s.write("/turn/run -250 0.14 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
        time.sleep(1)
        if  (x-16)<=0:
            s.write("/turn/run 200 0.91 \n".encode())
            time.sleep((16-x)*0.04)
            s.write("/stop/run \n".encode())
            time.sleep(1)
        else:
            s.write("/turn/run -200 0.91 \n".encode())
            time.sleep((x-16)*0.04)
            s.write("/stop/run \n".encode())
            time.sleep(1)
        
        s.write("/turn/run -250 -0.19 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
        time.sleep(1)

        s.write("/turn/run -200 0.91 \n".encode())
        time.sleep((y-16)*0.04)
        s.write("/stop/run \n".encode())
    elif d=='north':
        s.write("/turn/run 250 0.14 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
        time.sleep(1)

        if  (x-16)<=0:
            s.write("/turn/run 200 0.91 \n".encode())
            time.sleep((16-x)*0.04)
            s.write("/stop/run \n".encode())
            time.sleep(1)
        else:
            s.write("/turn/run -200 0.91 \n".encode())
            time.sleep((x-16)*0.04)
            s.write("/stop/run \n".encode())
            time.sleep(1)
        
        s.write("/turn/run -250 -0.19 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
        time.sleep(1)

        s.write("/turn/run -200 0.91 \n".encode())
        time.sleep((y-16)*0.04)
        s.write("/stop/run \n".encode())

        break
        