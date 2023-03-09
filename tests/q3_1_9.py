OK_FORMAT = True

test = {   'name': 'q3_1_9',
    'points': [1, 1],
    'suites': [   {   'cases': [   {'code': ">>> genre_and_distances.take(np.arange(7)).groupby('Genre').count().loc[my_assigned_genre][0]>= 4\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> my_assigned_genre == 'comedy'\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
