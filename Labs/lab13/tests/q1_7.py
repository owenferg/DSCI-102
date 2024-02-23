OK_FORMAT = True

test = {   'name': 'q1_7',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> all([type(lower_bound_pc) '
                                               'in set([float, np.float32, '
                                               'np.float64]), \n'
                                               '...     type(upper_bound_pc) '
                                               'in set([float, np.float32, '
                                               'np.float64]),\n'
                                               '...     type(reject) == '
                                               'bool])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all([lower_bound_pc == '
                                               'np.percentile(resampled_correlations_pc, '
                                               '2.5), \n'
                                               '...      upper_bound_pc == '
                                               'np.percentile(resampled_correlations_pc, '
                                               '97.5),\n'
                                               '...     reject == True])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
