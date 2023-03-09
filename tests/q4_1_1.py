OK_FORMAT = True

test = {   'name': 'q4_1_1',
    'points': [10],
    'suites': [   {   'cases': [   {   'code': '>>> fit_knn_t = KNN(X,y) \n'
                                               '>>> fit_knn_t.fit(tune_fit="yes")\n'
                                               '>>> pred_knn = fit_knn_t.predict() \n'
                                               '>>> assert fit_knn_t.model is not None\n'
                                               '>>> assert fit_knn_t.best_params != {}\n'
                                               '>>> assert fit_knn_t.best_score > 0\n'
                                               '>>> assert isinstance(pred_knn, np.ndarray)\n'
                                               '>>> assert len(pred_knn) == len(fit_knn_t.y_test)\n'
                                               '>>> accuracy, report = fit_knn_t.score()\n'
                                               '>>> assert isinstance(report, str)\n'
                                               '>>> assert accuracy >= 0 and accuracy <= 1\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
