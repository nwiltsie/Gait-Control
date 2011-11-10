//This code requires the arduino to be loaded with ServoFirmata. 
import processing.serial.*;
import cc.arduino.*;
Arduino arduino;

int legPin = 9; // Control pin for servo motor
int wingPin = 10;

void setup(){
  size (180, 180);
  arduino = new Arduino(this, Arduino.list()[0]);
  arduino.pinMode(legPin, Arduino.OUTPUT);
  arduino.pinMode(wingPin,Arduino.OUTPUT);
  // note - we are setting a digital pin to output
}

void draw(){
  arduino.analogWrite(legPin, mouseX); // the servo moves to the horizontal location of the mouse
  arduino.analogWrite(wingPin, mouseY); // the servo moves to the horizontal location of the mouse
  print(mouseX + " " + mouseY + "\n");
}
