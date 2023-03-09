OK_FORMAT = True

test = {   'name': 'q3_2_1',
    'points': [1.5, 1.5],
    'suites': [   {   'cases': [   {   'code': '>>> # This test just checks to see if your classify function works correctly \n'
                                               '>>> # with k=5 nearest neighbors.\n'
                                               '>>> from collections import Counter\n'
                                               ">>> g = train_movies['Genre']\n"
                                               '>>> def check(r, k):\n'
                                               '...     t = test_my_features.iloc[r]\n'
                                               "...     return classify(t, train_my_features, g, k) == most_common(pd.DataFrame({'Genre': g,'Distance':fast_distances(t, "
                                               "train_my_features)}).sort_values('Distance')[:k],'Genre')\n"
                                               '>>> check_5_nn = [check(i, 5) for i in np.arange(11)]\n'
                                               '>>> all(check_5_nn)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # This test just checks to see if your classify function works correctly \n'
                                               '>>> # with k=11 nearest neighbors.\n'
                                               '>>> from collections import Counter\n'
                                               ">>> g = train_movies['Genre']\n"
                                               '>>> def check(r, k):\n'
                                               '...     t = test_my_features.iloc[r]\n'
                                               '...     return classify(t, train_my_features, g, k) == most_common(pd.DataFrame(np.take(g, np.argsort(fast_distances(t, train_my_features))[:k])), '
                                               "'Genre')\n"
                                               '>>> check_11_nn = [check(i, 11) for i in np.arange(3)]\n'
                                               '>>> all(check_11_nn)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
