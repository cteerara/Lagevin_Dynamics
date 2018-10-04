import LagInput
import LagIO


def RK4(RHS, lagin, F):
  # INPUT:  Function RHS
  #         LagInput lagin
  #         tuple F
  # Takes the Right-Hand_side of an equation \frac{dx}{dt} = RHS(x,t) which the function will integrate. 
  # Step size is defined in lagin under dt.
  # F is the input to the RHS function. 
  # The first argument of RHS MUST always be the initial condition of the function you want to integrate.
  F0 = F[0]
  F_list = list(F)

  k1 = RHS(*F)
  F1 = F0 + k1*lagin.dt/2.0
  F_list[0] = F1
  F = tuple(F_list)  

  k2 = RHS(*F)
  F2 = F0 + k2*lagin.dt/2.0
  F_list[0] = F2
  F = tuple(F_list)

  k3 = RHS(*F)
  F3 = F0 + k3*lagin.dt
  F_list[0] = F3
  F = tuple(F_list) 

  k4 = RHS(*F)
  Fn = F0 + (k1+2*k2+2*k3+k4)*lagin.dt/6.0
  return Fn

