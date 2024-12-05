// Arduino IDLE

#include <Stepper.h>

int pin1 = 0;
int pin2 = 0;
int pin3 = 0;
int pin4 = 0;

int SPU = 0;
Stepper Motor1(SPU, pin1, pin2, pin3, pin4);

void setup()
{
    Motor1.setSpeed(5);
}

void loop()
{
    Motor1.step(SPU); // 360 Grad da SPU = Anzahl Schritte für 1 Umdrehung
    delay(1000);
    Motor1.step(-SPU);
    delay(1000);
}
