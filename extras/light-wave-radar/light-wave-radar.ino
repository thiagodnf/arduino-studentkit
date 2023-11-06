// include the Servo library
#include <Servo.h>

// name Arduino board pins used by the circuit
const int sensorPin = A0;
const int servoPin = 3;
const int potPin = A1;
const int LEDPin = 10;
const int buttonPin = 2;

const int greenLedPin = 10;
const int redLedPin = 9;

// declare variables
int lightAmount = 0;
int servoAngle = 0;
int inputCommand = 0;
int lightLow = 1023;
int lightHigh = 0;
int angleLow = 180;
int angleHigh = 0;

int increment = 5;
int incrementDelay = 50;
int potValue;
bool isRunning = false;
bool increase = true;

int index = 0;
const byte speed[] = {1, 2, 4, 6, 9};

Servo myServo;  // create a servo object

void setup() {

  pinMode(LEDPin, OUTPUT);
  pinMode(potPin, INPUT);
  pinMode(buttonPin, INPUT);

  pinMode(greenLedPin, OUTPUT);
  pinMode(redLedPin, OUTPUT);

  attachInterrupt(digitalPinToInterrupt(buttonPin), turnOn, RISING);

  // start the serial monitor
  Serial.begin(9600);

  myServo.attach(servoPin);   // attaches the servo on pin 3 to the servo object
  myServo.write(servoAngle);  // move the servo to the starting position

  digitalWrite(greenLedPin, LOW);
  digitalWrite(redLedPin, HIGH);

  delay(1000);
}

int readPot() {

  potValue = analogRead(potPin);

  index = map(potValue, 0, 1023, 0, 4);

  return speed[index];
}

void loop() {

  increment = readPot();
  incrementDelay = increment * 10;

  if (!isRunning) {
    digitalWrite(greenLedPin, LOW);
    digitalWrite(redLedPin, HIGH);
    return;
  }else{
    digitalWrite(greenLedPin, HIGH);
    digitalWrite(redLedPin, LOW);
  }

  servoAngle += increase ? increment : -increment;

  myServo.write(servoAngle);
  delay(incrementDelay);

  collectData();
  printData();

  if (servoAngle >= 180 || servoAngle <= 0) {
    increase = !increase;
  }

  delay(10);
}

void collectData() {

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

void turnOn() {

  isRunning = !isRunning;
}