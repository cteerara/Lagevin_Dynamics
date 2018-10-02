import LagInput 
import os

def readInput(filename):
  os.chdir("../input") 
  fid = open("Lag.in","r")
  for line in fid.readlines():
    # Line Parsed
    lp = line.split();
    if not not lp: # Handle empty strings. Python is weird...
      if lp[0] == "IniPos":
        IniPos = float(lp[1])
      elif lp[0] == "IniVel":
        IniVel = float(lp[1])
      elif lp[0] == "IniTemp":
        IniTemp = float(lp[1])
      elif lp[0] == "DampCoef":
        DampCoef = float(lp[1]);
      elif lp[0] == "dt":
        dt = float(lp[1])
      elif lp[0] == "ttot":
        ttot = int(lp[1]);
  os.chdir("../Lagevin")  
#  print(IniPos)
#  print(IniVel)
#  print(IniTemp)
#  print(DampCoef)
#  print(dt)
#  print(ttot)
  laginput = LagInput.get_LagInput(IniPos, IniVel, IniTemp, DampCoef, dt, ttot)
  return laginput

def writeOutput(fid, runID, time, pos, vel):
  if not os.path.isdir("../output"): # Not output directory
    os.mkdir("../output")

  os.chdir("../output")
  fid.write("%d\t%f\t%f\t%f\n" %(runID, time, pos, vel))
  os.chdir("../Lagevin")
