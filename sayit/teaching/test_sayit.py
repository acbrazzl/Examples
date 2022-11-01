import logging
import unittest
import argparse
import sayit

class TestSayit(unittest.TestCase):

    def test_say(self):
        sayit.say('test_success')

    #TODO: implement failure test of say

    #TODO: implement argparse wrap of sayit.py
