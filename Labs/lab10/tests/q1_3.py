OK_FORMAT = True

test = {
  'name': 'q1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs(sum(faithful_standard["duration (standard units)"])) <= 1e-8
          True
          >>> int(round(duration_std))
          1
          >>> int(round(wait_std))
          14
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
