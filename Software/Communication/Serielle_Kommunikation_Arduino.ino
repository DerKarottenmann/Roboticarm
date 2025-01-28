#include<string.h>
#include<Arduino.h>
#include "Servo.h"


Servo Servomotor1;

void setup()
{
  Servomotor1.attach(8);
  Serial.begin(9600);
  Servomotor1.write(0);


}

void loop() 
{   
  Servomotor1.write(0);
  if (Serial.available() > 0) {
    String inputString = Serial.readStringUntil('\n');
    Serial.println("Echo:" + inputString);
    String substrMotor = inputString.substring(0, 1);
    String IntsubstrDegrees = inputString.substring(1);
    int substrDegrees =  IntsubstrDegrees.toInt();

    if (substrMotor == "A") {
      Servomotor1.write(substrDegrees);
      delay(6000);
    }
  } 


} 