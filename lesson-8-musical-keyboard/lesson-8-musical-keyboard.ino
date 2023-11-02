// declare variables
int rate = 500;
int frequency = 1000000 / (rate * 2);

// name Arduino board pins used by the circuit
const int notePin = A0;
const int togglePin = 3;
const int buzzerPin = 8;

// declare variables
int keyVal = 0;       // stores the analog value from the resistor ladder
int key = 0;          // stores the button that is pressed
int switchState = 0;  // stores the state of the toggle button
int note = 0;         // stores which note should be played
int oldNote = 0;      // stores the previous note that was played

// an array of notes with frequencies of middle 
//               C,   D,   E,   F,   G,   A,   B,  high C
int notes[] = { 262, 294, 330, 349, 392, 440, 494, 523 };

void setup() {

  // set up pins as INPUTS or OUTPUTS
  pinMode(togglePin, INPUT);
  pinMode(buzzerPin, OUTPUT);

  // open a serial connection to the computer
  Serial.begin(9600);
}

void loop() {
  // read the inputs from the Arduino board
  
  keyVal = analogRead(notePin);          // analog value of the key
  switchState = digitalRead(togglePin);  // toggle button state

  if (keyVal > 1005) {        // first key is pressed
    key = 1;
  } else if (keyVal > 900) {  // second key is pressed
    key = 2;
  } else if (keyVal > 800) {  // third key is pressed
    key = 3;
  } else if (keyVal > 400) {  // fourth key is pressed
    key = 4;
  } else {                    // no key is pressed
    key = 0;
  }

  // determine the note to play based on if the toggle button is up or down
  switch (switchState) {
    case 0:
      // button is not pressed so play low notes (0 through 3)
      note = key - 1;
      break;
    case 1:
      // button is pressed so play high notes (4 through 7)
      note = key + 3;
      break;
  }

  // if a key is pressed, play the corresponding sound; 
  // otherwise, don't play anything
  if (key > 0) {
    tone(buzzerPin, notes[note]);
  } else {
    noTone(buzzerPin);
  }
}