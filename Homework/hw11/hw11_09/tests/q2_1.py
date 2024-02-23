OK_FORMAT = True


test = {   'name': 'q2_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Your resample should '
                                               'have the same number of rows '
                                               'as the original sample;\n'
                                               '>>> '
                                               'simulate_resample(observations).shape[0]\n'
                                               '17',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Your resample should '
                                               'only have the ;\n'
                                               '>>> '
                                               'simulate_resample(observations).columns[0] '
                                               '== observations.columns[0] \n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
