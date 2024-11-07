import os
import sys
import unittest
import pyaudio
import wave

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
class Test(unittest.TestCase):  
    def test_init(self):
        print("Hello from test.py")
        p = pyaudio.PyAudio()
        print(p.get_device_count())
        p.terminate()

 
if __name__ == '__main__':
    unittest.main()