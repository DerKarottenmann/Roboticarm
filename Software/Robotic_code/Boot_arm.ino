#include<string.h>
#include<Arduino.h>
#include "Servo.h"

int servo_pin1 = 8;
int servo_pin2 = 8;
int servo_pin3 = 8;
int servo_pin4 = 8;


void setup() {
    Serial.begin(9600);
    Servomotor1.attach(servo_pin1);
    Servomotor2.attach(servo_pin2);
    Servomotor3.attach(servo_pin3);
    Servomotor4.attach(servo_pin4);
    Servomotor1.write(45);
    Servomotor2.write(20);
    Servomotor3.write(0);
    Servomotor4.write(30);

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

    if (substrMotor == "B") {
      Servomotor2.write(substrDegrees);
      delay(6000);
    }

    if (substrMotor == "C") {
      Servomotor3.write(substrDegrees);
      delay(6000);
    }

    if (substrMotor == "D") {
      Servomotor4.write(substrDegrees);
      delay(6000);
    }

   
  } 


} 