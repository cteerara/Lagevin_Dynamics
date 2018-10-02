import LagInput
import LagIO
import LagRHS
import random
import LagIntegrator as LInt
import numpy as np
import matplotlib.pyplot as plt
lagin = LagIO.LagIO_readInput("Lag.in")

# Defining velocity function
def vel_RHS(v,t):
  # INPUT: LagInput lagin 
  #        Double rand
  #        Double v
  # OUTPUT: Double output
  # Function compute the Right-Hand-Side of the Lagevin velocity equation
  # \frac{dv(t)}{dt} = -\frac{\gamma}{m}v(t) + \frac{1}{m} \epsilon (t)
  
  epsilon_var = 2*lagin.IniTemp*lagin.DampCoef
  epsilon_std = np.sqrt(epsilon_var)
  epsilon = np.random.normal(0,epsilon_std,1)
  RHS = -lagin.DampCoef*v + epsilon
  return RHS
 
def pos_RHS(x0,v,t):
  # \frac{dx(t)}{dt} = v(t)
  return v

WallBound = 5

#------------------------------------------------------
# Main Loop
V = [0] * lagin.ttot
X = [0] * lagin.ttot
V[0] = lagin.IniVel
X[0] = lagin.IniPos

NumOfRun = 100
TimeHitWall = [0] * NumOfRun
tvec = np.linspace(0,lagin.ttot*lagin.dt,num=lagin.ttot)

for j in range(0,NumOfRun):
  for i in range(1,lagin.ttot):
    t = lagin.dt*i
    if X[i-1] >= 0 and X[i-1] <= WallBound:  
      V[i] = LInt.RK4(vel_RHS, lagin, (V[i-1],t))
    else: # If particle hit the wall.
      V[i] = 0
      TimeHitWall[j] = t
      break
    Vin = V[i]
    X[i] = LInt.RK4(pos_RHS, lagin, (X[i-1],Vin,t))
  

  plt.figure(200)
  plt.plot(tvec[0:i-1],X[0:i-1])
  
  plt.figure(300)
  plt.plot(tvec[0:i-1],V[0:i-1])



plt.figure(200)
plt.title('Position')
plt.xlabel('Time')
plt.ylabel('Position')

plt.figure(300)
plt.title('Velocity')
plt.xlabel('Time')
plt.ylabel('Velocity')

n_bins = 20
plt.figure(100)
plt.title('Time until particle hit the wall')
plt.hist(TimeHitWall, bins=n_bins)


plt.show()

#plt.figure(300)
#plt.title("Velocity")
#plt.show() 
#plt.figure(200)
#plt.title("Position")
#plt.show()
