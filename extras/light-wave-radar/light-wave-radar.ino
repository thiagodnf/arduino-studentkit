// include the Servo library
#include <Servo.h>

// name Arduino board pins used by the circuit
const byte sensorPin = A1;
const byte potPin = A0;
const byte beaconPin = 4;
const byte servoPin = 3;

// Light Sensor
int lightAmount = 0;

// Timer
byte beaconState = LOW;
unsigned long currentMillis = 0;
unsigned long previousMillis = 0;
int delayTime = 700;

// Servo
Servo myServo;
int servoSpeed = 0;
int servoAngle = 0;
int servoIncrement = 1;
int servoSpeeds[] = { 45, 35, 25, 15, 5 };

void setup() {

  pinMode(potPin, INPUT);
  pinMode(beaconPin, OUTPUT);
  pinMode(sensorPin, INPUT);

  // start the serial monitor
  Serial.begin(9600);

  // attaches the servo on pin 3 to the servo object
  myServo.attach(servoPin);
  // move the servo to the starting position
  myServo.write(servoAngle);

  delay(500);
}

int readPotValue() {
  return map(analogRead(potPin), 0, 1023, 0, 5);
}

void runServo() {

  servoAngle += servoIncrement;

  myServo.write(servoAngle);
  delay(servoSpeeds[servoSpeed - 1]);

  if (servoAngle >= 180 || servoAngle <= 0) {
    servoIncrement = -1 * servoIncrement;
  }
}

void loop() {

  // record the time from the timer
  currentMillis = millis();

  if (currentMillis - previousMillis >= delayTime) {
    // save the last time you blinked the LED
    previousMillis = currentMillis;

    beaconState = beaconState == LOW ? HIGH : LOW;

    // set the LED with the ledState of the variable:
    digitalWrite(beaconPin, beaconState);
  }

  servoSpeed = readPotValue();

  if (servoSpeed == 0) {
    delay(10);
    return;
  }

  runServo();
  collectData();
}

void collectData() {

  // read the light sensor and store the measurement in a variable
  lightAmount = analogRead(sensorPin);

  Serial.print(servoAngle);
  Serial.print(",");
  Serial.println(lightAmount);
}