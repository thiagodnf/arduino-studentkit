#include <Servo.h> // include the Servo library

Servo myServo; // create a servo object called myServo

// name pins used in the circuit
const int onButtonPin = 3;
const int servoPin = 11;
const int potPin = A4;
const int LEDPin = 9;

// declare variable
int wiperState = 0;
int potValue = 0;
int delayTime = 0;
long timerCount = 0;
int buttonState = 0;
int lastButtonState = 0;
int servoAngle = 0;

void setup()
{
    // declare pins used on Arduino as INPUTS or OUTPUTS
    pinMode(onButtonPin, INPUT);
    pinMode(LEDPin, OUTPUT);
    myServo.attach(servoPin);

    // open a serial connection to the computer
    Serial.begin(9600);

    // move the servo to the down position
    myServo.write(0);
}

void loop()
{

    // store value from potentiometer
    potValue = analogRead(potPin);

    // print information to the serial monitor
    Serial.print(wiperState);
    Serial.print(" : ");
    Serial.print(potValue);
    Serial.print(" : ");
    Serial.println(delayTime);

    // set the wiper mode based on the wiperState variable
    switch (wiperState)
    {
    // case 0 is when the wiper is off
    case 0:
        servoAngle = 0;
        delayTime = 1000;
        break;

    // case 1 is when the wiper is on
    case 1:
        // if the wiper is down, move it up; if the wiper is up, move it down
        if (servoAngle == 0)
        {
            servoAngle = 179;
        }
        else
        {
            servoAngle = 0;
        }
        delayTime = 1000;
        break;

    // case 2 is when the wiper is on the intermittent setting - move the wiper with a pause between wipes
    case 2:
        // if the wiper is down, move it up; if the wiper is up, move it down
        if (servoAngle == 0)
        {
            servoAngle = 179;
            delayTime = 1000;
        }
        else
        {
            servoAngle = 0;
            // set the delayTime based on the potentiometer
            delayTime = map(potValue, 0, 1023, 1000, 6000);
        }
        break;
    // case 3 is when the wiper is on the washer setting
    case 3:
        // turn on the wiper fluid
        digitalWrite(LEDPin, HIGH);

        // repeat the wash cycles 5 times
        for (int i = 0; i < 5; i = i + 1)
        {
            myServo.write(179);
            delay(1000);
            myServo.write(0);
            delay(1000);
        }
        // turn off the wiper fluid
        digitalWrite(LEDPin, LOW);
        wiperState = 0;
        break;
    }

    // move the wiper to the correct angle
    myServo.write(servoAngle);

    // record the time from the timer
    timerCount = millis();

    // loop for the delayTime number of milliseconds to wait for the wiper to move
    while (millis() < timerCount + delayTime)
    {
        buttonState = digitalRead(onButtonPin); // store the button state

        if (buttonState != lastButtonState)
        {                                  // if the button has changed states:
            lastButtonState = buttonState; // set the old state as the new state
            // change the wiperState if the button is pressed
            if (buttonState == HIGH)
            {
                wiperState = wiperState + 1;
                if (wiperState >= 4)
                {
                    wiperState = 0;
                }
                delay(50);
            }
        }
    }
}
