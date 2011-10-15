from __future__ import division
from config import STEP_PATTERN, RESET, MOVEMENT_TIMES

class GaitTable:
    '''A GaitTable is a list of (time, servo, position) tuples. The table
    represents one entire walking cycle for the robot (each leg moving through
    its full range), and it is meant to be executed repeatedly.'''
    def __init__(self, robot):
        self.robot = robot
        self.current_time = 0
        self.table = []
        for limb in self.robot.limbs:
            for event in RESET:
                self.add_entry(event, sequential = False)
        for limb in self.robot.limbs:
            self.add_step(limb)

    def add_step(self, limb):
        for event in STEP_PATTERN:
            self.add_entry(event)
    
    def add_entry(self, event, sequential = True):
        self.table.append((self.current_time, 
                           limb.joints[event[0]].servo,
                           limb.joints[event[0]].positions[event[1]]))
        if sequential:
            self.current_time += MOVEMENT_TIMES[event[1]]

    def __iter__(self):
        return self.table
