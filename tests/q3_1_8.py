OK_FORMAT = True

test = {   'name': 'q3_1_8',
    'points': [0, 1, 2],
    'suites': [   {   'cases': [   {'code': ">>> (genre_and_distances.columns == ['Genre', 'Distance']).all()\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> genre_and_distances.shape[0] == 283\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.allclose(genre_and_distances['Distance'], sorted(fast_distances(test_my_features.iloc[0], train_my_features)))\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
