#include "mbed.h"
#include "stdlib.h"
#include "bbcar.h"
#include "bbcar_rpc.h"

Ticker servo_ticker;
PwmOut pin5(D10), pin6(D11);
BBCar car(pin5, pin6, servo_ticker);
BufferedSerial pc(USBTX,USBRX); //tx,rx
BufferedSerial uart(D1,D0); //tx,rx


int main(){
   char buf[10];
   uart.set_baud(9600);
   int i=0;
   float angle=0;

   car.goStraight(-30);

   while(1){
      if(uart.readable()){
            char recv[1];
            uart.read(recv, sizeof(recv));
            buf[i++]=recv[0];

            if(recv[0] == '\n'){
                angle = atof(buf);
                i=0;
                double shift=angle-185; 
                printf("%f\n",angle);
                if(shift>10){
                    car.turn(-30,-0.9);
                    ThisThread::sleep_for(300ms);
                    printf("left\n");
                }

                else if(shift<-10){
                    car.turn(-30,0.9);
                    ThisThread::sleep_for(300ms);
                    printf("right\n");
                }
                else {
                    car.goStraight(-30);
                    ThisThread::sleep_for(300ms);
                    printf("straight\n");
                }


            }

            //pc.write(recv, sizeof(recv));

      }
   }
}