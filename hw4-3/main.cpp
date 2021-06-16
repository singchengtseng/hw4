#include "mbed.h"
#include "stdlib.h"
#include "bbcar.h"
#include "bbcar_rpc.h"

Ticker servo_ticker;
PwmOut pin5(D10), pin6(D11);
BBCar car(pin5, pin6, servo_ticker);
BufferedSerial pc(USBTX,USBRX); //tx,rx
BufferedSerial uart(D1,D0); //tx,rx

DigitalInOut pin10(D9);

int main(){
   char buf[10];
   uart.set_baud(9600);
   int i=0;
   float angle=0;
   parallax_ping  ping1(pin10);
   while(1){
      
      if(uart.readable()){
            
            char recv[1];
            uart.read(recv, sizeof(recv));
            buf[i++]=recv[0];

            if(recv[0] == '\n'){
                angle = atof(buf);
                i=0;
                float shift=angle;
                if(shift>0.5){
                    car.turn(-30,-0.7);
                    ThisThread::sleep_for(300ms);
                    printf("left\n");
                    if((float)ping1<10)
                        {
                           car.stop();
                           break;
                        }
                }
                else if(shift<-0.5){
                    car.turn(-30,0.8);
                    ThisThread::sleep_for(300ms);
                    printf("right\n");
                    if((float)ping1<10)
                        {
                           car.stop();
                           break;
                        }
                }
                else {
                     parallax_ping  ping1(pin10);
                     car.goStraight(-30);
                     while(1) {
                        if((float)ping1<10)
                        {
                           car.stop();
                           break;
                        }
                        ThisThread::sleep_for(10ms);
                     }
                }
            }
      }
      else
      {
         car.stop();
      }
   }
}