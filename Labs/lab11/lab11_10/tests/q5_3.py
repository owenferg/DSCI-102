OK_FORMAT = True

test = {
  'name': 'q5_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose([predict_wait(x) for x in [1.5, 2.5, 3.5, 4.5]], [51.19121315943784, 57.33026416682361, 75.63157712935188, 81.13767919873055])
          True
          """,
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
