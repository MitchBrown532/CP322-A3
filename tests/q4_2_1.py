OK_FORMAT = True

test = {   'name': 'q4_2_1',
    'points': [10],
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> fit_rf_t = RandomForest(X,y) \n'
                                               '>>> fit_rf_t.fit(tune_fit="yes")\n'
                                               '>>> pred_rf = fit_rf_t.predict() \n'
                                               '>>> assert fit_rf_t.model is not None\n'
                                               '>>> assert fit_rf_t.best_params != {}\n'
                                               '>>> assert isinstance(pred_rf, np.ndarray)\n'
                                               '>>> assert len(pred_knn) == len(fit_rf_t.y_test)\n'
                                               '>>> accuracy, report = fit_rf_t.score()\n'
                                               '>>> assert isinstance(report, str)\n'
                                               '>>> assert accuracy >= 0 and accuracy <= 1\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
