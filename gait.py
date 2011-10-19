from __future__ import division
from config import STEP_PATTERN, RESET, DT, RESET_DURATION, LIMB_ORDER

class GaitTable:
    '''A GaitTable is a list of (time, servo, position) tuples. The table
    represents one entire walking cycle for the robot (each leg moving through
    its full range), and it is meant to be executed repeatedly.'''
    def __init__(self, robot):
        self.robot = robot
        self.current_time = 0
        self.total_cycle_time = 0
        self.table = []
        for limb_name in LIMB_ORDER:
            for event in RESET:
                self.add_entry(event, limb_name, wait_for_finish = False)
        self.current_time += RESET_DURATION
        for limb_name in LIMB_ORDER:
            self.add_step(limb_name)

    def add_step(self, limb_name):
        for event in STEP_PATTERN:
            self.add_entry(event, limb_name, wait_for_finish = True)
    
    def add_entry(self, event, limb_name, wait_for_finish = True):
        joint_name = event[0]
        position_name = event[1]
        speed = event[2]
        self.table.append((self.current_time, 
                           limb_name, 
                           joint_name, 
                           position_name,
                           speed))

        limb = self.robot.limbs[limb_name]
        joint = limb.joints[joint_name]
        position = joint.positions[position_name]
        if wait_for_finish:
            travel_dist = abs(joint.positions[position_name]
                              - joint.current_position)
            self.current_time += travel_dist / speed 
        self.total_cycle_time = self.current_time
        joint.current_position = position

    def __iter__(self):
        '''This allows us to call "for entry in gait_table:"'''
        return self.table.__iter__()
