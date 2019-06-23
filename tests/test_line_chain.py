import unittest

import line_chain


class MyTestCase(unittest.TestCase):
    def test_line_chain(self):
        chain = line_chain.factory(config=[{
            'mode': 'linear',
            'ratio': 0.8,
            'start': 0.2,
            'target': 0.4
        }])
        self.assertAlmostEqual(chain[0.0], 0.2)
        self.assertAlmostEqual(chain[0.4], 0.3)
        self.assertAlmostEqual(chain[0.8], 0.4)
        self.assertAlmostEqual(chain[1.0], 0.4)

        chain = line_chain.factory(config=[{
            'mode': 'linear',
            'ratio': 0.8,
            'start': 0.2,
            'target': 0.4
        }, {
            'mode': 'cosine',
            'ratio': 1.0,
            'target': 0.0  # start from previous target 0.4
        }])
        self.assertAlmostEqual(chain[0.0], 0.2)
        self.assertAlmostEqual(chain[0.4], 0.3)
        self.assertAlmostEqual(chain[0.8], 0.4)
        self.assertAlmostEqual(chain[0.9], 0.2)
        self.assertAlmostEqual(chain[1.0], 0.0)

        chain = line_chain.factory(config=[{
            'mode': 'fixed',
            'ratio': 0.8,
            'target': 0.4
        }, {
            'mode': 'cosine',
            'ratio': 1.0,
            'start': 0.2,
            'target': 0.0
        }])
        self.assertAlmostEqual(chain[0.0], 0.4)
        self.assertAlmostEqual(chain[0.4], 0.4)
        self.assertAlmostEqual(chain[0.8], 0.4)
        self.assertAlmostEqual(chain[0.9], 0.1)
        self.assertAlmostEqual(chain[1.0], 0.0)

        self.assertTrue(str(chain).startswith('LineChain'))


if __name__ == '__main__':
    unittest.main()
