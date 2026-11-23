import unittest
from multiprocessing.forkserver import read_signed

import television
from television import *

class TVTester(unittest.TestCase):
    def test_init(self):
        result = Television()
        self.assertEqual(result.__str__(), "Power = False, Channel = 0, Volume = 0")

    def test_power(self):
        result = Television()
        self.assertEqual(result.__str__(), "Power = False, Channel = 0, Volume = 0")
        result.power()
        self.assertEqual(result.__str__(), "Power = True, Channel = 0, Volume = 0")
    def test_vol(self):
        result = Television()
        result.power()
        result.volume_up()
        result.volume_up()
        self.assertEqual(result.__str__(), "Power = True, Channel = 0, Volume = 2")
        result.volume_down()
        result.volume_down()
        self.assertEqual(result.__str__(), "Power = True, Channel = 0, Volume = 0")
        result.volume_up()
        result.volume_up()
        result.volume_up()
        result.volume_up()
        self.assertEqual(result.__str__(), "Power = True, Channel = 0, Volume = 2")
        result.volume_down()
        result.volume_down()
        result.volume_down()
        result.volume_down()
        self.assertEqual(result.__str__(), "Power = True, Channel = 0, Volume = 0")
    def test_channel(self):
        result = Television()
        result.power()
        result.channel_up()
        result.channel_up()
        self.assertEqual(result.__str__(), "Power = True, Channel = 2, Volume = 0")
        result.channel_down()
        result.channel_down()
        self.assertEqual(result.__str__(), "Power = True, Channel = 0, Volume = 0")
        result.channel_up()
        result.channel_up()
        result.channel_up()
        result.channel_up()
        self.assertEqual(result.__str__(), "Power = True, Channel = 0, Volume = 0")
        result.channel_down()
        result.channel_down()
        result.channel_down()
        result.channel_down()
        self.assertEqual(result.__str__(), "Power = True, Channel = 0, Volume = 0")
    def test_mute(self):
        result = Television()
        self.assertEqual(result.__str__(), "Power = False, Channel = 0, Volume = 0")
        result.mute()
        self.assertEqual(result.__str__(), "Power = False, Channel = 0, Volume = 0")
        result.power()
        result.volume_up()
        result.mute()
        self.assertEqual(result.__str__(), "Power = True, Channel = 0, Volume = 0")
        result.mute()
        self.assertEqual(result.__str__(), "Power = True, Channel = 0, Volume = 1")
if __name__ == '__main__':
    unittest.main()
