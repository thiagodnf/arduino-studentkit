int readValue = 0;
int writeValue = 0;

void setup() {
  pinMode(9, OUTPUT);   // declare the first LED pin as output
  pinMode(10, OUTPUT);  // declare the second LED pin as output
  pinMode(11, OUTPUT);  // declare the third LED pin as output
  Serial.begin(9600);
}
void loop() {
  readValue = analogRead(A0);  // store the value from the potentiometer
  writeValue = readValue / 4;  // divide the readValue by 4 and store as the writeValue  if (readValue < 300) {

  if (readValue < 300) {
    analogWrite(9, 0);   // turn off the first LED
    analogWrite(10, 0);  // turn off the second LED
    analogWrite(11, 0);  // turn off the third LED
  } else if (readValue < 600) {
    analogWrite(9, writeValue);  // turn on the first LED
    analogWrite(10, 0);          // turn off the second LED
    analogWrite(11, 0);          // turn off the third LED
  } else if (readValue < 900) {
    analogWrite(9, writeValue);   // turn on the first LED
    analogWrite(10, writeValue);  // turn on the second LED
    analogWrite(11, 0);           // turn off the third LED
  } else {
    analogWrite(9, writeValue);   // turn on the first LED
    analogWrite(10, writeValue);  // turn on the second LED
    analogWrite(11, writeValue);  // turn on the third LED
  }
  Serial.print(readValue);
  Serial.print(" : ");
  Serial.println(writeValue);
  delay(100);
}