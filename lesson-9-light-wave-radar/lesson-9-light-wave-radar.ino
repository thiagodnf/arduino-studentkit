// include the Servo library
#include <Servo.h>

// name Arduino board pins used by the circuit
const int sensorPin = A0;
const int servoPin = 3;
const int LEDPin = 10;

// declare variables
int lightAmount = 0;
int servoAngle = 0;
int inputCommand = 0;
int lightLow = 1023;
int lightHigh = 0;
int angleLow = 180;
int angleHigh = 0;
int increment = 5;

Servo myServo;  // create a servo object

void setup() {

  pinMode(LEDPin, OUTPUT);
  // start the serial monitor
  Serial.begin(9600);

  myServo.attach(servoPin);   // attaches the servo on pin 3 to the servo object
  myServo.write(servoAngle);  // move the servo to the starting position

  delay(1000);
}

void loop() {
  // set the servo position
  for (servoAngle = 0; servoAngle <= 180; servoAngle = servoAngle + increment) {
    collectData();
    printData();
  }
  for (servoAngle = 180; servoAngle >= 0; servoAngle = servoAngle - increment) {
    collectData();
    printData();
  }
}

void collectData() {
  // move the servo to the correct angle
  myServo.write(servoAngle);
  delay(500);

  // read the light sensor and store the measurement in a variable
  lightAmount = analogRead(sensorPin);

  // if the light measurement is a min or max, store it as the new min or max
  if (lightAmount > lightHigh) {
    lightHigh = lightAmount;
    angleHigh = servoAngle;
  }
  if (lightAmount < lightLow) {
    lightLow = lightAmount;
    angleLow = servoAngle;
  }
}

void printData() {
  // print out the values to the serial monitor
  Serial.print("Angle:");
  Serial.print(servoAngle);
  Serial.print(",Light Intensity:");
  Serial.print(lightAmount);
  Serial.print(",High:");
  Serial.print(lightHigh);
  Serial.print(",angleHigh:");
  Serial.print(angleHigh);
  Serial.print(",Low:");
  Serial.print(lightLow);
  Serial.print(",angleLow:");
  Serial.print(angleLow);
  Serial.println("");
}
