import LagIntegrator as LInt
#import matplotlib.pyplot as plt
import LagIO
import LagInput
import numpy as np
import matplotlib.pyplot as plt

lagin = LagIO.LagIO_readInput("Lag.in")

def RHS(y,t):
  return y*t

F0 = 2.0
F = F0
t = 1
a = np.linspace(0.0,0.0,num=lagin.ttot)
a[0] = F0
for i in range(1,lagin.ttot):
  t = lagin.dt * i
  F = LInt.RK4(RHS, lagin, (F,t))
  a[i] = F
  print(a[i])

t = np.linspace(0,1,num=lagin.ttot)

Fact = F0*np.exp(t**2/2)
plt.plot(t,a,'r.')
plt.plot(t,Fact,'b')
plt.show()
