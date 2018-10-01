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
 
 
V0 = lagin.IniVel
V = V0

#------------------------------------------------------
# Main Loop
V_vec = np.linspace(0.0,0.0,num=lagin.ttot)
for i in range(0,int(lagin.ttot)):
  t = lagin.dt*i
  V = LInt.RK4(vel_RHS, lagin, V,t)
  V_vec[i] = V

plt.plot(V_vec)
plt.show() 
