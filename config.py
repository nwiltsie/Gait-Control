from __future__ import division

# Firware update step size (must be equal to the value defined in
# firmware/firmware.pde
DT = 10

# Speed of each movement in degrees/second 
MOVEMENT_SPEEDS = {'up': 180,
                  'down': 180,
                  'forward': 180,
                  'back': 180,
                  'extend': 180,
                  'retract': 180,
                  'shimmy': 180,
                  'reset': 180}

# Servos, listed by their number according to the Arduino firmware
SERVOS = {0: {'limb': 'RF', 
              'joint': 'elbow',
              'positions': {'forward': 0,
                            'back': 180,
                            'shimmy': 170}},
          1: {'limb': 'RF',
              'joint': 'shoulder',
              'positions': {'up': 0,
                            'down': 170}},
          2: {'limb': 'RF',
              'joint': 'magnet',
              'positions': {'extend': 0,
                            'retract': 180}},
          3: {'limb': 'LF',
              'joint': 'elbow',
              'positions': {'forward': 0,
                            'back': 180,
                            'shimmy': 170}},
          4: {'limb': 'LF',
              'joint': 'shoulder',
              'positions': {'up': 0,
                            'down': 170}},
          5: {'limb': 'LF',
              'joint': 'magnet',
              'positions': {'extend': 0,
                            'retract': 180}},
          6: {'limb': 'LR',
              'joint': 'elbow',
              'positions': {'forward': 0,
                            'back': 180,
                            'shimmy': 170}},
          7: {'limb': 'LR',
              'joint': 'shoulder',
              'positions': {'up': 0,
                            'down': 170}},
          8: {'limb': 'LR',
              'joint': 'magnet',
              'positions': {'extend': 0,
                            'retract': 180}},
          9: {'limb': 'RR',
              'joint': 'elbow',
              'positions': {'forward': 0,
                            'back': 180,
                            'shimmy': 170}},
          10: {'limb': 'RR',
              'joint': 'shoulder',
              'positions': {'up': 0,
                            'down': 170}},
          11: {'limb': 'RR',
              'joint': 'magnet',
              'positions': {'extend': 0,
                            'retract': 180}}}

STEP_PATTERN =  [('magnet', 'retract'),
                 ('shoulder', 'up'),
                 ('magnet', 'extend'),
                 ('shoulder', 'down'),
                 ('elbow', 'shimmy'),
                 ('elbow', 'back'),
                 ('shoulder', 'up'),
                 ('elbow', 'forward'),
                 ('shoulder', 'down'),
                 ('magnet', 'extend')]

RESET = [('elbow', 'back'),
         ('magnet', 'extend'),
         ('shoulder', 'down')]

INITIAL = {'elbow': 'forward',
           'magnet': 'extend',
           'shoulder': 'down'}
