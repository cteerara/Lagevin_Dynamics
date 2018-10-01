import LagInput
import LagIO
import LagRHS
import random
import LagIntegrator

lin = LagIO.LagIO_read("Lag.in")
v = lin.IniVel
x0 = lin.IniPos
for i in range(0,lin.ttot):

  rand = random.uniform(0,1)
  v = Integrator.RK4(lin, rand, v, "vel")
  x = Integrator.RK4(lin, rand, v, "pos")
  print(x)
  
  

