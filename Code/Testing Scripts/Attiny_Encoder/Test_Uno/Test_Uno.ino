#include <Wire.h>
#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3);

void setup() {
  Serial.begin(9600);
  //Wire.begin();
  mySerial.begin(9600);
  pinMode(2, INPUT);
  pinMode(3, OUTPUT);

}

void loop() {
  //Wire.requestFrom(10, 1);    // request 6 bytes from slave device #2

  if (mySerial.available())
  {
    Serial.println(mySerial.read());
  }
    
}
