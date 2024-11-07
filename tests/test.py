import unittest
import pyaudio
import wave

class Test(unittest.TestCase):  
    def test_init(self):
        print("Hello from test.py")
        p = pyaudio.PyAudio()
        print(p.get_device_count())
        p.terminate()

 
if __name__ == '__main__':
    unittest.main()