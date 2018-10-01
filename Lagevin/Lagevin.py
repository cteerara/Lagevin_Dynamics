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
print(V[0],X[0])

tvec = np.linspace(0,lagin.ttot*lagin.dt,num=lagin.ttot)
for i in range(1,lagin.ttot):
  t = lagin.dt*i
  if X[i-1] > 0 and X[i-1] < WallBound:  
    V[i] = LInt.RK4(vel_RHS, lagin, (V[i-1],t))
  else:
    V[i] = 0
  Vin = V[i]
  X[i] = LInt.RK4(pos_RHS, lagin, (X[i-1],Vin,t))

plt.subplot(2,1,1)
plt.title("Position (top), Velocity (Bottom)")
plt.plot(tvec,X)
plt.subplot(2,1,2)
plt.plot(tvec,V)
plt.show() 
