OK_FORMAT = True


test = {   'name': 'q3_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> type(left_end_1) in '
                                               'set([float, np.float32, '
                                               'np.float64]) and '
                                               'type(right_end_1) in '
                                               'set([float, np.float32, '
                                               'np.float64])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> left_end_1 == '
                                               'np.percentile(bootstrap_mean_based_estimates, '
                                               ' 2.5)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> right_end_1 == '
                                               'np.percentile(bootstrap_mean_based_estimates, '
                                               ' 97.5)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
