import LagIntegrator as LInt
#import matplotlib.pyplot as plt
import LagIO
import LagInput
import numpy as np


lagin = LagIO.LagIO_readInput("Lag.in")

def RHS(y):
  return y

F0 = 1.0
F = F0
for i in range(0,100):
  F = LInt.RK4(RHS, lagin, F)
  print(F)
