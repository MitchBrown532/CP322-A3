OK_FORMAT = True

test = {   'name': 'q3_0',
    'points': [0.5, 0.5, 0],
    'suites': [   {   'cases': [   {'code': '>>> 0.0 <= distance_first_to_second <= 0.1\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(distance(np.array([1,2]), np.array([1,2])), 0)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(distance(np.array([1,2,3]), np.array([2,4,5])), 3)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
