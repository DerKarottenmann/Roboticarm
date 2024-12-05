#include <Servo.h>
Servo motor12;

void setup()
{
  motor12.attach(12);
  Serial.begin(9600);
}
String command;
int angle;
const float pi = 3.141592;
float x_value;
float y_value;
float a, b, c;
float test;
const int X_pin = A0;
const int Y_pin = A1;

void loop()
{
  if (Serial.available() > 0)
  {
    command = Serial.readString();
    command.trim();
    angle = command.toInt();
    if (angle >= 0 && angle <= 180)
    {
      motor12.write(angle);
    }
  }
  x_value = analogRead(X_pin) - 522;
  y_value = analogRead(Y_pin) - 506;

  a = x_value;
  b = y_value * -1;
  test = atan(b / a);
  test = (test / (2 * pi)) * 360;
  if (test < 0)
  {
    test += 180;
  }
  else if (isnan(test))
  {
    test = 90;
  }

  Serial.print(a);
  Serial.print("|");
  Serial.print(b);
  Serial.print("=");
  Serial.print(test);
  Serial.print("\n");
  motor12.write(test);
  delay(500);

  /* angle = analogRead(X_pin);
  angle = map(angle, 0, 1023, 0, 180);
  motor12.write(angle);
  delay(500);*/
}