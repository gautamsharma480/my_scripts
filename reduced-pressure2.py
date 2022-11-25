
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
amu = 1.67262192e-27 #Kg
kB = 1.380649e-23 # J/K
T = 298.0 #K
kBT = kB*T
Rc=6.46e-10 #m

rho=[1,2,3,4,5,6,7,8]
def P_reduced2phy(p_reduced):
    GPa=1e+9 #Pa
    p_reduced = p_reduced*kBT/Rc**3
    return p_reduced/GPa

#p_Neimark = 70 # in reduced units
#print(P_reduced2phy(p_Neimark), "GPa")

def P_phy2reduced(p_physical):
    GPa=1e+9 #Pa
    p_reduced = p_physical*GPa*Rc**3/kBT
    return p_reduced


def cals_excess_P(P_arr,a): # Deliver output in reduced units
    excess_P=[] 
    # J. Chem. Phys., 107, 11, 1997
    # This script reproduces the Fig. 3 of the above paper.

    P_reduced=[]
    for i in P_arr:
        P_reduced.append(P_phy2reduced(i))
        #print(rho[i], (P_reduced[i] - rho[i]) / a)
    for i in range(0,len(P_reduced)):
        excess_P.append((P_reduced[i] - rho[i]) / a)
    return excess_P

'''for j in P_15:
    P_30_reduced.append(P_phy2reduced(j))
for k in  P_30:
    P_15_reduced.append(P_phy2reduced(k))

a=25
y=[]
for i in range(0,len(P_15)):
    #print(P[i],"GPa",P_reduced[i])
    print(rho[i],(P_15_reduced[i]-rho[i])/a)
    y.append((P_15_reduced[i]-rho[i])/a)'''


#rho=[1,2,3,4,5,6,7,8]
# I obtained the pressure data below for water system using Materials Studio.
# (Computational details are adopted from J. Chem. Phys. 107, 11, 1997)
P_15 = [0.032,0.110,0.237,0.414,0.640,0.914,1.236,1.607] # in GPa
P_25=[0.040,0.159,0.364,0.650,1.017,1.464,1.992,2.602] # in GPa
P_30 = [0.043,0.183,0.428,0.769,1.206,1.741,2.372,3.100] # in GPa
P_75 = [0.068,0.409,1.020, 1.853,2.930,4.255,5.850,9.969] # in GPa
P_78 = [0.070, 0.425, 1.061, 1.926, 3.046, 4.426, 6.110, 11.063] # in GPa
P_15_reduced=cals_excess_P(P_15,15)
P_25_reduced=cals_excess_P(P_25,25)
P_30_reduced=cals_excess_P(P_30,30)
P_75_reduced=cals_excess_P(P_75,75)
P_78_reduced=cals_excess_P(P_78,78)
alpha = 0.101
f = [alpha*i**2 for i in rho]
plt.plot(rho,P_15_reduced, marker='x',label='a_15')
plt.plot(rho,P_25_reduced, marker='s',label='a_25')
plt.plot(rho,P_30_reduced, marker='o',label='a_30')
plt.plot(rho,P_75_reduced, marker='P',label='a_75')
plt.plot(rho,P_78_reduced, marker='P',label='a_78')
plt.plot(rho,f,marker='*', label=r'$\alpha\rho^2$')
plt.ylabel(r'(p-$\rho$*kT)/a',fontsize=20)
plt.xlabel(r'$\rho$', fontsize=20)
plt.xlim(0,10)
plt.ylim(0,8)
plt.legend()
plt.show()
