/* Bounce-Free Rotary Encoder

   David Johnson-Davies - www.technoblogy.com - 28th October 2017
   ATtiny85 @ 1 MHz (internal oscillator; BOD disabled)
   
   CC BY 4.0
   Licensed under a Creative Commons Attribution 4.0 International license: 
   http://creativecommons.org/licenses/by/4.0/
*/

//#include <TinyWire.h>

//byte own_address = 10;
unsigned long interval = 500; 
unsigned long previousMillis = 0;

const int EncoderA = 3;
const int EncoderB = 4;

// Rotary encoder **********************************************

volatile int a0;
volatile int c0;
volatile int Count = 0;

// Called when encoder value changes
void ChangeValue (bool Up) {
  Count = max(min((Count + (Up ? 1 : -1)), 1000), 0);
}

// Pin change interrupt service routine
ISR (PCINT0_vect) {
  int a = PINB>>EncoderA & 1;
  int b = PINB>>EncoderB & 1;
  if (a != a0) {              // A changed
    a0 = a;
    if (b != c0) {
      c0 = b;
      ChangeValue(a == b);
    }
  }
}



//void onI2CRequest() {
//  // sends one byte with content 'b' to the master, regardless how many bytes he expects
//  // if the buffer is empty, but the master is still requesting, the slave aborts the communication
//  // (so it is not blocking)
//  TinyWire.send('b');
//}
//
//void onI2CReceive(int howMany){
//  // loops, until all received bytes are read
//  while(TinyWire.available()>0){
//    // toggles the led everytime, when an 'a' is received
//    if(TinyWire.read()=='a'){
//      TinyWire.send('a');
//    }
//  }
//}

// Setup demo **********************************************

void setup() {
  //TinyWire.begin( own_address );
 // register a handler function in case of a request from a master
  //TinyWire.onRequest( onI2CRequest );
  //TinyWire.onReceive( onI2CReceive );
  Serial.begin(9600);
  pinMode(EncoderA, INPUT_PULLUP);
  pinMode(EncoderB, INPUT_PULLUP);
  PCMSK = 1<<EncoderA;        // Configure pin change interrupt on A
  GIMSK = 1<<PCIE;            // Enable interrupt
  GIFR = 1<<PCIF;             // Clear interrupt flag
}

void loop() {

  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    Serial.write(Count);
  }
  
}
