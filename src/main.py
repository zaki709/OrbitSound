import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from acoustic.HRTF import HRTF

def main():
    # load HRTF data
    hrtf = HRTF()
    hrtf.checkModel()
    hrtf.openData(hrtf.Lpath[0][0])
    hrtf.convHRTF2Np()


    

if __name__ == '__main__':
    main()