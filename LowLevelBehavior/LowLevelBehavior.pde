// Low-level Squishbot behavior
// Code by Nick Wiltsie

/* 
  Legs are counted by looking down at the top of the robot,
  going counter-clockwise from the front right.  This is the
  same as domains in polar coordinates (except with 0-based
  indexing).
  
  Forward-back leg servos are in array positions 0, 3, 6, 9.
  Wing servos are in positions 1, 4, 7, 10.
  Magnet servos are in positions 2, 5, 8, 11.
  
  Serial commands are two characters: a leg number and a
  command.  1W means move the "1" leg's "wing" up, and
  0w means move the "0" leg's "wing" down.  Leg and magnet
  commands are {L,l,M,m}.  Capital letters are for "active"
  motions - stepping out, lifting up, and activating the magnet.
*/



#include <Servo.h> 
 
Servo servos[12];  // create servo object to control a servo

byte in_pos[] = {10, 176, 5, 179};
byte out_pos[] = {176, 5, 179, 12};

byte up_pos[] = {106, 78, 107, 74};
byte down_pos[] = {80, 94, 97, 87};
  
byte on_pos[] = {160, 160, 160, 160};
byte off_pos[] = {160, 160, 160, 160};

byte command[3];
  
void setup() { 
  for (int i=0; i<12; i++){
    servos[i].attach(2+i, 800, 2200); 
  }
  
  Serial.begin(9600);
} 
 
 
void loop() { 
  while (Serial.available() < 2) {
      //Do nothing
  }
  
  byte leg_num = Serial.read() - 48;
  byte com = Serial.read();
  
  Serial.write(leg_num+48);
  Serial.write(com);

  
  if (leg_num >= 4 || !(com == 'l' || com == 'L' || com == 'w' || com == 'W' || com == 'm' || com == 'M')){
    Serial.println("Bad Command!");
  } else {
    Serial.println("Good Command!");
    switch (com){
      case 'l':
        servos[3*leg_num].write(in_pos[leg_num]);
        break;
      case 'L':
        servos[3*leg_num].write(out_pos[leg_num]);
        break;
      case 'w':
        servos[3*leg_num+1].write(down_pos[leg_num]);
        break;
      case 'W':
        servos[3*leg_num+1].write(up_pos[leg_num]);
        break;
      case 'm':
        servos[3*leg_num+2].write(off_pos[leg_num]);
        break;
      case 'M':
        servos[3*leg_num+2].write(on_pos[leg_num]);
        break; 
    }     
  }
  
  
//  Serial.print(leg_num, DEC);
//  for (byte i=0; i<leg_num; i++){
//    digitalWrite(13, HIGH);
//    delay(100);
//    digitalWrite(13, LOW);
//    delay(100);
//  }
}

void leg_in(byte leg_num) {
  servos[3*leg_num].write(in_pos[leg_num]);
}

void leg_out(byte leg_num) {
  servos[3*leg_num].write(out_pos[leg_num]);
}

void wing_up(int leg_num){
  servos[3*leg_num+1].write(up_pos[leg_num]);
}

void wing_down(byte leg_num){
  servos[3*leg_num+1].write(down_pos[leg_num]);
}

void magnet_on(byte leg_num){
  servos[3*leg_num+2].write(on_pos[leg_num]);
}

void magnet_off(byte leg_num){
  servos[3*leg_num+2].write(off_pos[leg_num]);
}
