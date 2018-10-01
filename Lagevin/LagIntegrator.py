import LagInput
import LagIO


def Lag_RK4(RHS, lagin, F0):
  k1 = RHS(F0)
  F1 = F0 + k1*lagin.dt/2.0
  
  k2 = RHS(F1)
  F2 = F0 + k2*lagin.dt/2.0

  k3 = RHS(F2)
  F3 = F0 + k3*lagin.dt

  k4 = RHS(F3)
  Fn = F0 + (k1+2*k2+2*k3+k4)*lagin.dt/6.0

  return Fn

