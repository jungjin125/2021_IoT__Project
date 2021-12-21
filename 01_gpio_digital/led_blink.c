#include <wiringPi.h>
#define LED_red 4
#define LED_yello 17
#define LED_green 26


int main (void)
{

  wiringPiSetupGpio () ;
  pinMode (LED_red, OUTPUT) ;
  
    digitalWrite (LED_red, HIGH) ; delay (1000) ;
    digitalWrite (LED_red,  LOW) ; delay (1000) ;
  pinMode (LED_yello, OUTPUT) ;
 
  
    digitalWrite (LED_yello, HIGH) ; delay (1000) ;
    digitalWrite (LED_yello,  LOW) ; delay (1000) ;
 
  pinMode (LED_green, OUTPUT) ;
 
 
    digitalWrite (LED_green, HIGH) ; delay (1000) ;
    digitalWrite (LED_green,  LOW) ; delay (1000) ;
 
  return 0 ;
}