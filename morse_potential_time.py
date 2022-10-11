import numpy as np
pi = 3.1415926
fs = 1e-15 # s
amu = 1.67e-27 #Kg
kB = 1.38e-23 # J/K
T = 298 #K
KT = kB*T
Rc = 4.45e-10 # m
a_width = 2/Rc   # Length_inverse
D_depth = 8.5*KT   # energy
m1 = 1 * amu
m2 = 18 * amu
# This code is help to find out time step to be used in classical molecular dynamics simulations.
# Generally, I can choose a time step (dt) = T * 0.01 
def rm(m1,m2):
    # Calculate reduced mass of two particle moving in Morse potential
    mr = m1 * m2 / (m1 + m2)
    print("reduced mass = ", mr/amu, "amu")
    return mr
def fc(a,D):
    # Force constant at the equilibrium of Morse potential
    ke = 2 * D * a ** 2
    print("force constant = ", ke, "N/m")
    return ke
def time_morse(mr, ke):
    # Time period for Morse potential at the equilibrium.
    T = 2 * pi * np.sqrt(mr/ke)
    return T/fs
print("time_period = ", time_morse(rm(m1,m2),fc(a_width,D_depth)), "fs")
