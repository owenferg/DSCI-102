OK_FORMAT = True

test = {   'name': 'q2_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure you assigned '
                                               '`binary_options` to an array;\n'
                                               '>>> type(binary_options) == '
                                               'np.ndarray\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Should be a two element '
                                               'array of a binary '
                                               'distribution;\n'
                                               '>>> '
                                               'sorted(set(binary_options)) == '
                                               'sorted(set([0, 1]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
