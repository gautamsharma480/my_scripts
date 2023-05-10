
import numpy as np
A = 1e-10 # m
kB = 1.38e-23 # j/K
rc = 4.48e-10
# rc = 6.46e-10
amu = 1.67e-27 #kg
T = 298 #K
fs = 1e-15 #s

m = 1 * amu
gamma  = 4.5 * np.sqrt(m*kB*T) / rc

print(gamma*fs/amu)
