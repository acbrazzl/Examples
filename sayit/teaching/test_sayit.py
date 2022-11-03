import logging
import unittest
import argparse
import sayit

args = sayit.get_parser().parse_args()

class TestSayit(unittest.TestCase):

    def test_say(self):
        sayit.say('test_success')

    #TODO: (2) implement failure test of say

    def test_sayit_empty_args(self):
        with self.assertRaises(SystemExit):
            sayit.main(args)

if __name__ == '__main__':
    unittest.main()
