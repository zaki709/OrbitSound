
import math
import numpy as np

from src.acoustic.HRTF import HRTF
from src.utils.config import configInit
Conf = configInit()


class spacialSound():
  def __init__(self):
    self.dataInit()
    self.StdSoundDis = 1.
    self.SoundDisMin = 0.2
  
  def dataInit(self):
    self.hrtf = HRTF()
    self.hrtfFreq = self.hrtf.readData(Conf.HRTFpath)
    self.elev = self.hrtf.readData(Conf.Elevpath)
    self.azimuth = self.hrtf.readData(Conf.Azimuthpath)
    self.StdDist = 1.4 #[m]

    self.npElev = np.array(self.elev)
    self.npAzi = []
    for aziList in self.azimuth:
      self.npAzi.append(np.array(aziList))

    

  def pos2spherialCoordinate(self, x, y, z):
    #x, y, z [m]
    if y >= 0:
      sgn = 1
    elif y < 0:
      sgn = -1
    try:
      azi = sgn * math.acos(x / math.sqrt(x ** 2 + y ** 2))
      if azi < 0:
        azi = np.pi - azi
    except ZeroDivisionError as e:
      azi = 0
    elev = math.asin(z / math.sqrt(x ** 2 + y ** 2 + z ** 2))
    
    return  elev * 180/np.pi, azi * 180/np.pi
  
  def distanceAtenuation(self, data, x, y, z):
    dis = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    if self.SoundDisMin > dis:
      return data/dis
    else:
      return data/self.SoundDisMin

  def getNearestDegIdx(self, elev, azi):
    #logger.debug("Input position deg: azi : {0}, elev : {1}".format(azi, elev))
    
    eleIdx = np.abs(self.npElev - elev).argmin()
    
    aziIdx = np.abs(self.npAzi[eleIdx] - azi).argmin()
    return eleIdx, aziIdx

  def getHRTF(self, x, y, z):
    ele, azi = self.pos2spherialCoordinate(x, y, z)
    eId, aId = self.getNearestDegIdx(ele, azi)
    Lhrtf = self.hrtfFreq[0][eId][aId]
    Rhrtf = self.hrtfFreq[1][eId][aId]
    return Lhrtf, Rhrtf

if __name__ == '__main__':
  
  hrtf = HRTF()
  hrtf.checkModel()
  hrtf.openData(hrtf.Lpath[0][0])
  hrtf.convHRTF2Np()
  """
  spec = spacialSound()
  ele, azi = spec.pos2spherialCoordinate(-1,-1,1)
  eId, aId = spec.getNearestDegIdx(ele, azi)

  print(ele, eId)
  print(azi, aId)
  """