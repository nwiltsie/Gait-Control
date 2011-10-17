from __future__ import division

# Firware update step size (must be equal to the value defined in
# firmware/firmware.pde
DT = 10

# Speed of each movement in degrees/second 
MOVEMENT_SPEEDS = {'up': 10,
                  'down': 10,
                  'forward': 10,
                  'back': 10,
                  'on': 10,
                  'off': 10,
                  'shimmy': 10,
                  'reset': 10}

# Servos, listed by their number according to the Arduino firmware
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

STEP_PATTERN =  [('magnet', 'off'),
                 ('shoulder', 'up'),
                 ('magnet', 'on'),
                 ('shoulder', 'down'),
                 ('elbow', 'shimmy'),
                 ('elbow', 'back'),
                 ('shoulder', 'up'),
                 ('elbow', 'forward'),
                 ('shoulder', 'down'),
                 ('magnet', 'on')]

RESET = [('elbow', 'back'),
         ('magnet', 'on'),
         ('shoulder', 'down')]

# seconds required to execute the reset motion at the beginning of each cycle
RESET_DURATION = 5 

INITIAL = {'elbow': 'forward',
           'magnet': 'on',
           'shoulder': 'down'}
