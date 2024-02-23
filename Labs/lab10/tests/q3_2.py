OK_FORMAT = True

test = {
  'name': 'q3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {   'code': '>>> np.array_equal(faithful_predictions.labels, ["duration", "wait", "predicted wait"])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
        {
          'code': '>>> abs(1 - np.mean(faithful_predictions["predicted wait"]/100)) <= 0.35\n'
          'True',
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
