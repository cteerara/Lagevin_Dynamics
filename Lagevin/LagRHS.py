# -*- coding: utf-8 -*-
import LagInput
import LagIO
#
## Lagevin input
#lin = LagIO.LagIO_read("Lag.in") 
#print(lin.IniPos)
# Lagevin velocity equation
def vel_RHS(lagin,rand, v):
  # INPUT: LagInput lagin 
  #        Double rand
  #        Double v
  # OUTPUT: Double output
  # Function compute the Right-Hand-Side of the Lagevin velocity equation
  # \frac{dv(t)}{dt} = -\frac{\gamma}{m}v(t) + \frac{1}{m} \epsilon (t)
  
  RHS = -lagin.DampCoef*v + rand 
  return RHS
  
