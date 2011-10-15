
MOVEMENT_TIMES = {'up': 1,
                  'down': 1,
                  'forward': 1,
                  'backward': 1,
                  'extend': 1,
                  'retract': 1,
                  'shimmy': 1,
                  'reset': 1}

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
                            'retract': 180}},

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

RESET = [('elbow': 'back')]
