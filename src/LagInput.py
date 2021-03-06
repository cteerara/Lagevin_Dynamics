class LagInput(object):
  IniPos = 0.0
  IniVel = 0.0
  IniTemp = 0.0
  DampCoef = 0.0
  dt = 0.0
  ttot = 0.0

  def __init__(self, IniPos, IniVel, IniTemp, DampCoef, dt, ttot):
    self.IniPos = IniPos
    self.IniVel = IniVel
    self.IniTemp = IniTemp
    self.DampCoef = DampCoef
    self.dt = dt
    self.ttot = ttot # Total timesteps

def get_LagInput(IniPos, IniVel, IniTemp, DampCoef, dt, ttot):
  #INPUT: double IniPos
  #       double IniVel
  #       double IniTemp
  #       double DampCoef
  #       double dt
  #       integer ttot
  laginput = LagInput(IniPos, IniVel, IniTemp, DampCoef, dt, ttot)
  return laginput
  
