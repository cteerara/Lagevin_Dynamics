import LagInput
import LagIO
import random
import LagIntegrator as LInt
import numpy as np
import matplotlib.pyplot as plt
import os
import argparse

#-------------------------------------------
def getInput():
  # Create and define input
  parser = argparse.ArgumentParser()
  parser.add_argument('--temperature', help='Input temperature of type double')
  parser.add_argument('--total_time', help='Input total time of type double')
  parser.add_argument('--time_step',help='Input time step size of type double')
  parser.add_argument('--initial_position', help='Input initial position of type double')
  parser.add_argument('--initial_velocity', help='Input initial velocity of type double')
  parser.add_argument('--damping_coefficient', help='Input damping coefficient of type double')

  args = parser.parse_args()
  filename = "Lag.in"	
  LagIO.writeInput(args,filename)
  lagin = LagIO.readInput(filename)
  return lagin

#---------------------------------------------
# Defining velocity function
def vel_RHS(v,lagin,t):
  # INPUT: double v
  #        LagInput lagin 
  #        Double t
  # OUTPUT: Double output
  # Function compute the Right-Hand-Side of the Lagevin velocity equation
  # \frac{dv(t)}{dt} = -\frac{\gamma}{m}v(t) + \frac{1}{m} \epsilon (t)
  # Where v is the initial velocity. lagin is the derived type variable containing all the inputs, and t is time
  epsilon_var = 2*lagin.IniTemp*lagin.DampCoef
  epsilon_std = np.sqrt(epsilon_var)
  epsilon = np.random.normal(0,epsilon_std,1)
  RHS = -lagin.DampCoef*v + epsilon
  return RHS

 
def pos_RHS(x0,v,t):
  # INPUT: double x0
  #        double v
  #        double t
  # Function compute the Right-Hand_Side of the position equation
  # \frac{dx(t)}{dt} = v(t)
  # Where x0 is the initial position, v is the velocity, and t is time
  return v


#------------------------------------------------------
def Main():
  #INPUT:   
  #OUTPUT:  integer PlotBlowUP
  # This is the main loop containing the integration and figure saving steps. It only output PlotBlowUp which is 1 when the velocity or the position goes to infinity and integration fails.
  PlotBlowUp=0
  lagin = getInput()
  WallBound = 5
  # Main Loop
  V = [0] * lagin.ttot
  X = [0] * lagin.ttot
  V[0] = lagin.IniVel
  X[0] = lagin.IniPos
	
  NumOfRun = 100
  TimeHitWall = [0] * NumOfRun
  tvec = np.linspace(0,lagin.ttot*lagin.dt,num=lagin.ttot)
	
  HighestTimeStep = 0
  Tajectory = [0]*lagin.ttot
	
  if not os.path.isdir("../output"):
    os.mkdir("../output")
	
  os.chdir("../output")
  fid = open("LagOut.out","w")
  fid.write("runID\ttime\tposition\tvelocity\n\n")
	
  for j in range(0,NumOfRun):
    for i in range(1,lagin.ttot):
      t = lagin.dt*i
      if X[i-1] >= 0 and X[i-1] <= WallBound:  
	      V[i] = LInt.RK4(vel_RHS, lagin, (V[i-1],lagin,t))
      else: # If particle hit the wall.
        V[i] = 0
        TimeHitWall[j] = t
        break
      Vin = V[i]
      X[i] = LInt.RK4(pos_RHS, lagin, (X[i-1],Vin,t))

      if np.isinf(V[i]) or np.isinf(X[i]):
        PlotBlowUp=1
        break
	    # Write output
      fid.write("%d\t%f\t%f\t%f\n"%(j+1,t,X[i],V[i]))
	  
	  # Write partition between runID
    fid.write("#### Run number %d complete ####\n\n"%(j+1))
	
	  # Save positions with longest staytime.
    if i>HighestTimeStep:
      HighestTimeStep = i
      for k in range(0,i):
        Tajectory[k] = X[k]
	
	#  plt.figure(400)
	#  plt.plot(tvec[0:i-1],X[0:i-1])
	#----------------------------------------------------
	# Save plots
  os.chdir("../output")
	
	# Plot Tajectory
  #plt.figure()
  plt.plot(tvec[0:HighestTimeStep-1],Tajectory[0:HighestTimeStep-1])
  plt.title("Tajectory")
  plt.savefig("Tajectory.png")
  plt.close()

	# Plot Histogram
  n_bins = 20
  #plt.figure()
  plt.title('Time until particle hit the wall')
  plt.hist(TimeHitWall, bins=n_bins)
  plt.savefig('Histogram.png')
  #plt.close() 
  #plt.show()
  os.chdir("../src")
  
  return PlotBlowUp
if __name__ == '__main__':
  Main()

