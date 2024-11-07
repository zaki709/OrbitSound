import os
import sys
import unittest
from src.acoustic.HRTF import HRTF

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
class TestHRTF(unittest.TestCase):
    def test_getModelNameList(self):
        hrtf = HRTF()
        hrtf.getModelNameList()
        self.assertTrue(len(hrtf.elev) > 0)
        print(hrtf.elev[0])
