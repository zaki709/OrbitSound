import unittest
from src.acoustic.HRTF import HRTF

class TestHRTF(unittest.TestCase):
    def test_getModelNameList(self):
        hrtf = HRTF()
        hrtf.getModelNameList()
        self.assertTrue(len(hrtf.elev) > 0)
