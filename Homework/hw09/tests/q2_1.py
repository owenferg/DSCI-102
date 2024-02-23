OK_FORMAT = True


test = {   'name': 'q2_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Your resample should '
                                               'have the same number of rows '
                                               'as the original sample;\n'
                                               '>>> '
                                               'len(simulate_resample(observations).rows)\n'
                                               '17',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.random.seed(50)\n'
                                               '>>> simulate_resample(observations).columns[0].item(3) == 108 \n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
