from __future__ import division
import time
import serial
from config import SERVOS
from robot import Robot
from gait import GaitTable

'''
Basic gait control program written by Robin Deits
'''

class RobotCommander:
    def __init__(self, robot, gait_table, device = '/dev/tty.usbmodemfd141'):
        self.gait_table = gait_table
        self.robot = robot
        # self.port = serial.Serial(port=self.device,
        #         baudrate=9600,
        #         bytesize=serial.EIGHTBITS,
        #         stopbits=serial.STOPBITS_ONE,
        #         parity=serial.PARITY_NONE,
        #         timeout=0.5,
        #         writeTimeout=0)

    def run(self):
        '''Walk continuously'''
        while True:
            self.execute_cycle()
            
    def execute_cycle(self):
        '''Reset, then step each of the four limbs'''
        self.cycle_start = time.time()
        for (entry_time, 
             limb_name, 
             joint_name, 
             position_name,
             speed) in self.gait_table:
            limb = self.robot.limbs[limb_name]
            joint = limb.joints[joint_name]
            servo = joint.servo
            position = joint.positions[position_name]
            cycle_time = time.time() - self.cycle_start
            if entry_time > cycle_time:
                time.sleep(entry_time - cycle_time)
            self.move(servo, position, speed)
        cycle_time = time.time() - self.cycle_start
        if cycle_time < self.gait_table.total_cycle_time:
            time.sleep(self.gait_table.total_cycle_time - cycle_time)

    def move(self, servo, position, speed):
        print "moving", servo, position, speed
        # self.port.write(servo)
        # self.port.write(position)
        # self.port.write(speed)


if __name__ == "__main__":
    robot = Robot()
    robot.register_servos(SERVOS)
    table = GaitTable(robot)
    for entry in table:
        print entry
    commander = RobotCommander(robot, table)
    commander.run()

