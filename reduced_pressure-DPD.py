
import numpy as np

amu = 1.67262192e-27 #Kg
kB = 1.380649e-23 # J/K
T = 298.0 #K
kBT = kB*T
Rc=6.46e-10 #m

def P_reduced2phy(p_reduced):
    GPa=1e+9 #Pa
    p_reduced = p_reduced*kBT/Rc**3
    return p_reduced/GPa

p_Neimark = 70 # in reduced units  ### THE JOURNAL OF CHEMICAL PHYSICS 148, 024108 (2018) ##
print(P_reduced2phy(p_Neimark), "GPa")

def P_phy2reduced(p_physical):
    GPa=1e+9 #Pa
    p_reduced = p_physical*GPa*Rc**3/kBT
    return p_reduced

P=[0.648, 0.701, 0.848, 0.969] # in GPa from Materials studio output.
P_reduced=[]
for i in P:
    P_reduced.append(P_phy2reduced(i))

for i in range(0,len(P)):
    print(P[i],"GPa",P_reduced[i])

