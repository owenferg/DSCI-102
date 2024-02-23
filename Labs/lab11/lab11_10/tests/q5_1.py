OK_FORMAT = True

test = {
  'name': 'q5_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose([below_3_r, above_3_r], [0.2805262439611597 , 0.3773941488382454])
          True
          >>> [below_3.shape[0], above_3.shape[0]]
          [97, 175]
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
