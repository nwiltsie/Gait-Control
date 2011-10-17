from __future__ import division
from config import STEP_PATTERN, RESET, MOVEMENT_TIMES

class GaitTable:
    '''A GaitTable is a list of (time, servo, position) tuples. The table
    represents one entire walking cycle for the robot (each leg moving through
    its full range), and it is meant to be executed repeatedly.'''
    def __init__(self, robot):
        self.robot = robot
        self.current_time = 0
        self.total_cycle_time = 0
        self.table = []
        for limb_name in self.robot.limbs:
            for event in RESET:
                self.add_entry(event, limb_name, wait_for_finish = False)
        for limb_name in self.robot.limbs:
            self.add_step(limb_name)

    def add_step(self, limb_name):
        for event in STEP_PATTERN:
            self.add_entry(event, limb_name, wait_for_finish = True)
    
    def add_entry(self, event, limb_name, wait_for_finish = True):
        limb = self.robot.limbs[limb_name]
        self.table.append((self.current_time, 
                           limb.joints[event[0]].servo,
                           limb.joints[event[0]].positions[event[1]]))
        if wait_for_finish:
            self.current_time += MOVEMENT_TIMES[event[1]]
        self.total_cycle_time = self.current_time

    def __iter__(self):
        return self.table.__iter__()
