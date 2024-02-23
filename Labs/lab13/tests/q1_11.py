OK_FORMAT = True

test = {   'name': 'q1_11',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> all([type(lower_bound_sal) '
                                               'in set([float, np.float32, '
                                               'np.float64]), \n'
                                               '...     type(upper_bound_sal) '
                                               'in set([float, np.float32, '
                                               'np.float64]),\n'
                                               '...     type(reject_sal) == '
                                               'bool])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all([lower_bound_sal == '
                                               'np.percentile(resampled_correlations_salary, '
                                               '2.5), \n'
                                               '...      upper_bound_sal == '
                                               'np.percentile(resampled_correlations_salary, '
                                               '97.5),\n'
                                               '...     reject_sal == True])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
