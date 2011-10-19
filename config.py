from __future__ import division

# Firware update step size (must be equal to the value defined in
# firmware/firmware.pde
DT = 10

# Servos, listed by their number according to the Arduino firmware.
# elbows move their respective limbs forward and backward,
# shoulders move them up and down
SERVOS = {0: {'limb': 'RF', 
              'joint': 'elbow',
              'positions': {'forward': 170,
                            'back': 10,
                            'shimmy': 30}},
          1: {'limb': 'RF',
              'joint': 'shoulder',
              'positions': {'up': 70,
                            'down': 50}},
          2: {'limb': 'RF',
              'joint': 'magnet',
              'positions': {'on': 68,
                            'off': 180}},
          3: {'limb': 'LF',
              'joint': 'elbow',
              'positions': {'forward': 10,
                            'back': 175,
                            'shimmy': 155}},
          4: {'limb': 'LF',
              'joint': 'shoulder',
              'positions': {'up': 13,
                            'down': 33}},
          5: {'limb': 'LF',
              'joint': 'magnet',
              'positions': {'on': 68,
                            'off': 180}},
          6: {'limb': 'LR',
              'joint': 'elbow',
              'positions': {'forward': 10,
                            'back': 175,
                            'shimmy': 155}},
          7: {'limb': 'LR',
              'joint': 'shoulder',
              'positions': {'up': 168,
                            'down': 148}},
          8: {'limb': 'LR',
              'joint': 'magnet',
              'positions': {'on': 68,
                            'off': 180}},
          9: {'limb': 'RR',
              'joint': 'elbow',
              'positions': {'forward': 170,
                            'back': 10,
                            'shimmy': 30}},
          10: {'limb': 'RR',
              'joint': 'shoulder',
              'positions': {'up': 131,
                            'down': 151}},
          11: {'limb': 'RR',
              'joint': 'magnet',
              'positions': {'on': 68,
                            'off': 180}}}

# Each entry in this list is a tuple of (joint, position, speed). They will be
# executed in sequence, each waiting for the previous to finish before starting,
# for each limb. Speed is given in degrees/second.
STEP_PATTERN =  [('magnet', 'off', 50),
                 ('shoulder', 'up', 50),
                 ('magnet', 'on', 50),
                 ('shoulder', 'down', 50),
                 ('elbow', 'shimmy', 50),
                 ('elbow', 'back', 50),
                 ('shoulder', 'up', 50),
                 ('elbow', 'forward', 50),
                 ('shoulder', 'down', 50),
                 ('magnet', 'on', 50)]

# The RESET list functions just like the step list, but it will be executed for
# all limbs simultaneously at the beginning of the cycle
RESET = [('elbow', 'back', 10),
         ('magnet', 'on', 10),
         ('shoulder', 'down', 10)]

# Seconds required to execute the reset motion at the beginning of each cycle
RESET_DURATION = 5 

# Initial configuration of each joint before the start of each cycle. 
INITIAL = {'elbow': 'forward',
           'magnet': 'on',
           'shoulder': 'down'}

# The order in which the limbs execute their steps
LIMB_ORDER = ['RF', 'LF', 'RR', 'LR']
