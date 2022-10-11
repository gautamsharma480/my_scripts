import numpy as np
import matplotlib.pyplot as plt
class Density:
   def __init__(self,a):
     self.a = a
     #print(a)
   @property
   def average(self):
     avg = sum(self.a) / len(self.a)
     #print("Average density =", avg, "g/cm^3")

     return avg
   def SD(self,avg):
     x = 0
     for i in self.a:
        x = x + (i-avg)**2
     SD = np.sqrt(x/len(self.a))
     SE = SD/np.sqrt(len(self.a))
     #print("SD =", SD)
     #print("SE =", SE)
     print("Average density = ", avg ,"\u00B1", SE, "g/cm^3")
     #return avg
      
      
# This is data of example 1.      
C200F402 = [1.70425813,1.79057900,1.75540363,1.73713983,1.80790996]
C100F202 = [1.81145905,1.73522053,1.88345777,1.87902603,1.73425864]
C50F102 = [1.81167164,1.75824542,1.76822773,1.85416863,1.85092407]
C25F52 = [1.98488471,2.09930998,2.00517305,1.96266781,1.92032799]
b = [C200F402,C100F202,C50F102,C25F52]
results = []
for i in range(0,len(b)):
    den = Density(b[i])
    den.SD(den.average)
    

# This is data of example 2.
msd_25_3p = [11.1494,10.0890,5.1115,6.7701,7.0746]
msd_50_3p = [6.1864,11.0016,4.9960,3.6928,9.8379]
msd_25_1p = [5.9815,12.8575,3.2921,3.8714,6.1851]
msd_50_1p = [3.9113,18.2468,6.6262,9.1110,3.2396]
msd = [msd_25_3p,msd_50_3p,msd_25_1p,msd_50_1p]
for i in range(0,4):
    avg = Density(msd[i])
    den.SD(avg.average)
