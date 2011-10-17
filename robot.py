from __future__ import division

from config import INITIAL

class Joint:
    def __init__(self, name, servo, positions):
        self.name = name
        self.servo = servo
        self.positions = positions
        self.current_position = None

class Limb:
    def __init__(self, name):
        self.name = name
        self.joints = {}

class Robot:
    '''A Robot is essentially a collection of limbs, each of which is a
    collection of joints and possible positions.'''
    def __init__(self):
        self.limbs = {}
    def register_servos(self, servos):
        for key in servos:
            limb_name = servos[key]['limb']
            joint_name = servos[key]['joint']
            positions = servos[key]['positions']
            if limb_name not in self.limbs:
                self.limbs.update({limb_name: Limb(limb_name)})
            limb = self.limbs[limb_name]
            limb.joints.update({joint_name: Joint(name = joint_name,
                                                  servo = key, 
                                                  positions = positions)})
            joint = limb.joints[joint_name]
            joint.current_position = joint.positions[INITIAL[joint_name]]
