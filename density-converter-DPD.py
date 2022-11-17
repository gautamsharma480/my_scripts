import numpy as np
# reduced density to physical and vice versa.
amu = 1.66e-27 #Kg
rho_reduced = 3
Rc = 6.46e-10 # meter
m = 100 * amu


def r2p(rho_reduced): # reduced to physical
    rho_physical = m*rho_reduced/Rc**3
    return "%.4f" % (rho_physical *1e-3) # g/cc

def p2r(rho_physical): # physical to reduced
    g = 1e-3 #kg
    cm = 1e-2 #m
    g_per_cc = g/cm**3
    rho_physical = rho_physical*g_per_cc
    rho_reduced = rho_physical * Rc**3 / m
    return "%.2f" % rho_reduced
rho = [3,4,5,6,7,8,9,10]

for i in rho:
    print(r2p(i), 'g/cc',(p2r(float(r2p(i)))))
    
