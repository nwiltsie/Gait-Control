from __future__ import division

class Joint:
    def __init__(self, servo, positions):
        self.servo = servo
        self.positions = positions

class Limb:
    def __init__(self):
        self.joints = {}

class Robot:
    '''A Robot is essentially a collection of limbs, each of which is a
    collection of joints and possible positions.'''
    def __init__(self):
        self.limbs = {}
    def register_servos(self, servos):
        for key in servos:
            limb = servos[key]['limb']
            joint = servos[key]['joint']
            positions = servos[key]['positions']
            if limb not in self.limbs:
                self.limbs.update({limb: Limb()})
            self.limbs[limb].joints.update({joint: Joint(servo = key,
                                                         positions = positions)})
