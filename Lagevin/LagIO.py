import LagInput 
import os

def readInput(filename):
  os.chdir("../input") 
  fid = open("Lag.in","r")
  for line in fid.readlines():
    # Line Parsed
    lp = line.split();
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

def writeInput(args):
  if not os.path.isdir("../input"):
    os.mkdir("../input")
  os.chdir("../input")
  fidin = open("Lag.in","w")
  for arg in vars(args):
    line = arg, getattr(args, arg)
    fidin.write("%s %s\n"%(arg, getattr(args,arg)))
  os.chdir("../Lagevin")
