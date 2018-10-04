import LagInput 
import os

def readInput(filename):
  os.chdir("../input") 
  fid = open(filename,"r")
  for line in fid.readlines():
    # Line Parsed
    lp = line.split();
    if lp[1] == 'None':
      print("Invalid input. Using default values")
      IniPos = 0.0
      IniVel = 0.0
      IniTemp = 0.0
      DampCoef = 0.0
      dt = 1
      ttot = 10
      break
    if not not lp: # Handle empty strings. Python is weird...
      if lp[0] == "initial_position":
        IniPos = float(lp[1])
      elif lp[0] == "initial_velocity":
        IniVel = float(lp[1])
      elif lp[0] == "temperature":
        IniTemp = float(lp[1])
      elif lp[0] == "damping_coefficient":
        DampCoef = float(lp[1]);
      elif lp[0] == "time_step":
        dt = float(lp[1])
      elif lp[0] == "total_time":
        ttot = float(lp[1]);

  #ttot is actually total time step which is equal to total_time/dt
  ttot = int(ttot/dt)
  os.chdir("../src")  
#  print(IniPos)
#  print(IniVel)
#  print(IniTemp)
#  print(DampCoef)
#  print(dt)
#  print(ttot)
  laginput = LagInput.get_LagInput(IniPos, IniVel, IniTemp, DampCoef, dt, ttot)
  return laginput

def writeInput(args,filename):
  if not os.path.isdir("../input"):
    os.mkdir("../input")
  os.chdir("../input")
  fidin = open(filename,"w")
  for arg in vars(args):
    line = arg, getattr(args, arg)
    fidin.write("%s %s\n"%(arg, getattr(args,arg)))
  os.chdir("../src")
