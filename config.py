from __future__ import division

# Firware update step size (must be equal to the value defined in
# firmware/firmware.pde
DT = 10

# Servos, listed by their number according to the Arduino firmware.
# elbows move their respective limbs forward and backward,
# shoulders move them up and down
SERVOS = {0: {'limb': 'RF', 
              'joint': 'elbow',
              'positions': {'forward': 176,
                            'back': 10,
                            'shimmy': 30}},
          1: {'limb': 'RF',
              'joint': 'shoulder',
              'positions': {'up': 106,
                            'down': 80}},
          2: {'limb': 'RF',
              'joint': 'magnet',
              'positions': {'on': 160,
                            'off': 160}},
          3: {'limb': 'LF',
              'joint': 'elbow',
              'positions': {'forward': 5,
                            'back': 176,
                            'shimmy': 156}},
          4: {'limb': 'LF',
              'joint': 'shoulder',
              'positions': {'up': 78,
                            'down': 94}},
          5: {'limb': 'LF',
              'joint': 'magnet',
              'positions': {'on': 160,
                            'off': 160}},
          6: {'limb': 'LR',
              'joint': 'elbow',
              'positions': {'forward': 5,
                            'back': 179,
                            'shimmy': 159}},
          7: {'limb': 'LR',
              'joint': 'shoulder',
              'positions': {'up': 107,
                            'down': 97}},
          8: {'limb': 'LR',
              'joint': 'magnet',
              'positions': {'on': 160,
                            'off': 160}},
          9: {'limb': 'RR',
              'joint': 'elbow',
              'positions': {'forward': 179,
                            'back': 12,
                            'shimmy': 32}},
          10: {'limb': 'RR',
              'joint': 'shoulder',
              'positions': {'up': 74,
                            'down': 87}},
          11: {'limb': 'RR',
              'joint': 'magnet',
              'positions': {'on': 160,
                            'off': 160}}}

# Each entry in this list is a tuple of (joint, position, speed). They will be
# executed in sequence, each waiting for the previous to finish before starting,
# for each limb. Speed is given in degrees/second.
STEP_PATTERN =  [('magnet', 'off', 10),
                 ('shoulder', 'up', 10),
                 ('magnet', 'on', 10),
                 ('shoulder', 'down', 10),
                 ('elbow', 'shimmy', 10),
                 ('elbow', 'back', 10),
                 ('shoulder', 'up', 10),
                 ('elbow', 'forward', 10),
                 ('shoulder', 'down', 10),
                 ('magnet', 'on', 10)]

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
