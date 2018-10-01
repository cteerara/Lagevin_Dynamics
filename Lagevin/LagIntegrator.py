import LagInput
import LagIO


def RK4(RHS, lagin, F0, t):
  k1 = RHS(F0,t)
  F1 = F0 + k1*lagin.dt/2.0
  
  k2 = RHS(F1,t)
  F2 = F0 + k2*lagin.dt/2.0

  k3 = RHS(F2,t)
  F3 = F0 + k3*lagin.dt

  k4 = RHS(F3,t)
  Fn = F0 + (k1+2*k2+2*k3+k4)*lagin.dt/6.0

  return Fn

