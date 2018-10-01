# -*- coding: utf-8 -*-
import LagInput
import LagIO
import numpy as np
#
## Lagevin input
#lin = LagIO.LagIO_read("Lag.in") 
#print(lin.IniPos)
# Lagevin velocity equation
def vel_RHS(lagin):
  # INPUT: LagInput lagin 
  #        Double rand
  #        Double v
  # OUTPUT: Double output
  # Function compute the Right-Hand-Side of the Lagevin velocity equation
  # \frac{dv(t)}{dt} = -\frac{\gamma}{m}v(t) + \frac{1}{m} \epsilon (t)
  
  epsilon_var = 2*lagin.IniTemp*lagin.DampCoef
  epsilon_std = np.sqrt(var)
  epsilon = np.random.normal(0,epsilon_std,1)
  RHS = -lagin.DampCoef*v + epsilon
  return RHS
  
