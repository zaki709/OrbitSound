import os
import sys
import re
import pyaudio
import numpy as np

from utils.config import configInit
Conf = configInit()
logger = Conf.setLogger(__name__)


"""
        Head F
          x
          ^
Left　<-- z  Right

http://www.sp.m.is.nagoya-u.ac.jp/HRTF/
HRTF data (2)

中部TLO
E-mail: ctlo@nisri.jp
ID Number: NU-0234 (頭部音響伝達関数データベース)
西野隆典, 梶田将司, 武田一哉, 板倉文忠, "水平方向及び仰角方向に関 する頭部伝達関数の補間," 日本音響学会誌, 57巻, 11号, pp.685-692, 2001.
"""


class HRTF:
    def __init__(self) -> None:
        self.elev = []
        self.azimuth = []
        self.Lpath = []
        self.Rpath = []
        self.hrtf = [[], []]
        self.left = 0
        self.right = 1

    def checkModel(self) -> None:
        if os.path.isdir(Conf.HRTFmodel):
            logger.info(f'{Conf.HRTFmodel} is found.')
        else:
            logger.error(f'{Conf.HRTFmodel} is not found.')
            exit(-1)

    def getModelNameList(self):
        dirList = os.listdir(Conf.HRTFmodel)
        dirList = sorted(dirList)

        for dirname in dirList:
            if dirname.startswith("elev"):
                self.elev.append(dirname.replace("elev", ""))
                dir = os.path.join(Conf.HRTFmodel, dirname)
                fileList = os.listdir(dir)
                fileList = sorted(fileList)
                azimuth = []
                Lpath = []
                Rpath = []
                for fileName in fileList:
                    path = os.path.join(dir, fileName)
                    name,ext = os.path.splitext(fileName)
                    if ext == '.dat':
                        if name.startswith("L"):
                            ele = int(re.findall('L(.*)e', name)[0])
                            azi = int(re.findall('e(.*)a', name)[0])
                            azimuth.append(azi)
                            Lpath.append(path)
                        elif name.startswith("R"):
                            Rpath.append(path)
                self.azimuth.append(azimuth)
                self.Lpath.append(Lpath)
                self.Rpath.append(Rpath)
    
        sorted_ind = [*range(len(self.elev))]
        sorted_ind.sort(key=lambda x: int(self.elev[x]))
        self.elev = [self.elev[i] for i in sorted_ind]
        self.azimuth = [self.azim[i] for i in sorted_ind]

        self.Lpath = [self.Lpath[i] for i in sorted_ind]
        self.Rpath = [self.Rpath[i] for i in sorted_ind]