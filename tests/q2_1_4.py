OK_FORMAT = True

test = {   'name': 'q2_1_4',
    'points': [1, 0, 1],
    'suites': [   {   'cases': [   {'code': ">>> set(close_movies.columns) >= {'Genre', 'Title', 'feel', 'water'}\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> close_movies.shape[0] == 5\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> close_movies["Title"].iloc[0] != "monty python and the holy grail" # Make sure that you are using the training set.\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
