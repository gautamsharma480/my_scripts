import matplotlib.pyplot as plt
import numpy as np

kB = 1.38e-23 # J/K
T = 298 #K
KT = kB*T #kcal/mol
f=open('file.dat','w')
RC = 1#4.45e-10
RM = 0.45 * RC
R0 = 0.22 * RC
A = -8.88
K = 8.5 #* KT

def my_func(low,up,leng):
    list = []
    step = (up - low) / float(leng)
    for i in range(leng):
        list.append(low)
        low = low + step
    return list

R = my_func(0, 1,100)

def morse_potential(R):
    #R = R*RC
    if R<RM:
        #print(R)
        U1 = K*(1-np.exp(A*(R-R0)))**2  - K*(1-np.exp(A*(RM-R0)))**2
    else:
        U1 = 0
    R2 = 1-R
    if R2 < RM:
        U2 = K*(1-np.exp(A*(R2-R0)))**2  - K*(1-np.exp(A*(RM-R0)))**2
    else:
        U2 = 0
    print(R,U1,U2)
    U = U1 + U2
    return U

U = []
for i in R:
    #print(i,morse_potential(i))
    #if i < RM:
        U.append(morse_potential(i))
        f.write(str(i) + ' ' + str(morse_potential(i))+'\n')
    #else:
    #    U.append(0)
f.close()
plt.plot(R, U)
#plt.ylim([-10,10])
#plt.xlim([0,1])
plt.xlabel('R ')
plt.ylabel('Energy ')
plt.show()
