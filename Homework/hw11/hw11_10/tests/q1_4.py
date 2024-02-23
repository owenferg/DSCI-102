OK_FORMAT = True

test = {   'name': 'q1_4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> np.isclose(correlation([1,2,3], '
                                               '[4,5,6]), 1, .001)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isclose(correlation([-3, 0, 3], '
                                               '[-3, 0, 3]), 1, .001)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
