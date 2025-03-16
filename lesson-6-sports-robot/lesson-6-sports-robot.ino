#include <Servo.h>        // include the Servo library

Servo myServo;            // create a servo object called myServo

const int potPin = A0;    // set the name of pin A0 to potPin
const int buttonPin = 7;  // set the name of pin 7 to buttonPin
int potValue = 0;         // variable to read the value from the potentiometer
int servoAngle = 0;       // variable to set the angle for the servo motor

void setup() {
  myServo.attach(9);   // attaches the servo on pin 9 to the myServo object
  Serial.begin(9600);  // open a serial connection to the computer
}

void loop() {
  
  if (digitalRead(buttonPin) == HIGH) {           // if the button is pressed:
    myServo.write(179);                           // move the servo to kick the ball
  } else {                                        // the button is not pressed:
    potValue = analogRead(potPin);                // store the potentiometer value in a variable
    servoAngle = map(potValue, 0, 1023, 0, 179);  // scale potentiometer value to the servo
    myServo.write(servoAngle);                    // turn the servo to the angle variable
  }
  
  Serial.print("potValue: ");      // print a label for the potValue variable
  Serial.print(potValue);          // print the potValue variable
  Serial.print(", servoAngle: ");  // print a label for the servoAngle variable
  Serial.println(servoAngle);      // print the servoAngle variable
  
  delay(100);                      // wait for the servo to get there
}