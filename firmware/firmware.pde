/* Firmware for the robot written by Robin Deits. 
   The robot receives serial commands from a master computer, which sends data
   in (servo, position) pairs. */

//Original description from Nick Wiltsie:
/* 
  Legs are counted by looking down at the top of the robot,
  going counter-clockwise from the front right.  This is the
  same as domains in polar coordinates (except with 0-based
  indexing).
  
  Forward-back leg servos are in array positions 0, 3, 6, 9.
  Wing servos are in positions 1, 4, 7, 10.
  Magnet servos are in positions 2, 5, 8, 11.
*/

#include <Servo.h>

#define NUM_SERVOS 12
#define BAUD_RATE 9600
uint8_t desired_positions[NUM_SERVOS];
uint8_t current_positions[NUM_SERVOS];

#define DT 10 //ms per step, MUST be the same as DT in config.py

uint8_t step_sizes[NUM_SERVOS] =  {
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1}; //degrees per step

uint8_t i;

uint8_t current_servo = 0;

Servo servos[NUM_SERVOS];

void setup() { 
  for (i=0; i<NUM_SERVOS; i++){
    servos[i].attach(2+i, 800, 2200); 
  }
  
  Serial.begin(BAUD_RATE);
} 
 
void loop() { 
    if (Serial.available() >= 3) {
        current_servo = Serial.read();
        desired_positions[current_servo] = Serial.read();
        step_sizes[current_servo] = Serial.read();
    }
    for(i = 0; i < NUM_SERVOS, i++) {
        if (current_positions[i] <= desired_positions[i]) {
            if ((desired_positions[i] - current_positions[i]) <= step_sizes[i]) {
                current_positions[i] = desired_positions[i];
            }
            else {
                current_positions[i] += step_sizes[i];
            }
        }
        else {
            if ((current_positions[i] - desired_positions[i]) <= step_sizes[i]) {
                current_positions[i] = desired_positions[i];
            }
            else {
                current_positions[i] -= step_sizes[i];
            }
        }
        servos[i].write(current_positions[i]);
    }
    delay(DT);
}




