import numpy as np
import matplotlib.pyplot as plt

# Following data is obtained from The Journal of Chemical Physics 148, 024108 (2018)

# Proton diffusion data from Neimark's paper
data_Neimark_P = np.loadtxt('7.dat') # Fig. 7 
lam2= data_Neimark_P[:,0]
D_ratio_Neimark_P = data_Neimark_P[:,1]


# Following data is obtained from The Journal of Chemical Physics 148, 024108 (2018)
# Water diffusion data from Neimark's paper
data_Neimark_water = np.loadtxt('5.dat') # Fig. 5 
lam3=data_Neimark_water[:,0]
D_ratio_Neimark_water=data_Neimark_water[:,1]

# Lambda values used by me in the data
lam = [0,0.5,1,1.5,2,4,8,16] # 8 elements
# from lam[0] = 0 from lam list to plot D_ratio_water
# bulk water diffusion coefficient
Db=2.0032*3

#following data is obtained using Materials Studio by DPD calculations
# The Journal of Chemical Physics 148, 024108 (2018)

#D_ratio = [0.3411/Db,0.4450/Db,0.3013/Db,0.1722/Db,0.1777/Db,0.4974/Db,1.0669/Db]
#D_ratio_water = []
#D_ratio = [0.2476/Db,0.3861/Db,0.3838/Db,0.3671/Db, 0.1722/Db,0.1777/Db,0.4974/Db,1.0669/Db] #NPT
#D_ratio_water = [2.616e-2/Db,3.784e-2/Db,5.272e-2/Db, 4.074e-2/Db,7.507e-2/Db,0.2035/Db,0.4308/Db] # NPT
#D_ratio = [6.936e-2/Db,0.1483/Db,0.1741/Db,0.1733/Db,0.1722/Db,0.1777/Db,0.4974/Db,1.0669/Db,1.5560/Db]
#D_ratio_water = [3.207e-2/Db,3.801e-2/Db,4.832e-2/Db,4.074e-2/Db,7.507e-2/Db,0.2035/Db,0.4308/Db,0.8696/Db]
#D_ratio_Nafion = [3.084e-3/Db,6.397e-3/Db,6.217e-3/Db,6.255e-3/Db,2.905e-3/Db,3.163e-3/Db,3.779e-3/Db,4.845e-3/Db] # with Grottuss
#D_ratio_Nafion = [4.989e-3/Db,5.500e-3/Db,5.298e-3/Db,5.666e-3/Db,2.662e-3/Db,2.740e-3/Db,3.618e-3/Db,5.027e-3/Db] #wo Grotthuss
#D_ratio = [7.3306e-2/Db,8.936e-2/Db,9.132e-2/Db,0.1122/Db,0.1077/Db,0.1981/Db,0.6414/Db,1.4591/Db] # wo grotthuss
#D_ratio_water = [2.734e-2/Db,3.363e-2/Db,4.132e-2/Db,3.696e-2/Db,7.099e-2/Db,0.1870/Db,0.4287/Db] # wo grothuss

D_proton = [7.3306e-2,8.936e-2,9.132e-2,0.1122,0.1077,0.1981,0.6414,1.4591] # 8 elements
D_water = [4.739e-2,5.319e-2,5.801e-2,6.581e-2,0.1012,0.2144,0.4834] # 7 elements
D_Nafion = [7.977e-3,8.210e-3,8.46e-3,8.078e-3,8.625e-3,8.067e-3,7.349e-3,7.474e-3] # 8 elements

D_ratio_p = [i/Db for i in D_proton]
D_ratio_water =  [i/Db for i in D_water]
D_ratio_Nafion = [i/Db for i in D_Nafion]
#print(out_array)
def my_data_vs_edgar():
    edgar = [0.2536,0.3955,2.5478,2.4882]
    log_edgar = np.log10(edgar)
    log_array_p = np.log10(D_ratio_p)
    plt.plot(lam, log_array_p,marker='o',label='my')
    plt.plot(lam, log_edgar,marker='o',label='Edgar')

def plot_proton():
    log_array_p = np.log10(D_ratio_p)
    plt.plot(lam,log_array_p,marker='o',label='my')
    plt.plot(lam2,D_ratio_Neimark_P,marker='x',label='Neimark')
    plt.ylim([-5,0])
    plt.xlabel('lambda')
    plt.ylabel('log10(Dp/Dw)')
    plt.legend()

def plot_water():
    log_array_water = np.log10(D_ratio_water)
    plt.plot(lam,log_array_water,marker='o',label='my')
    plt.plot(lam3,D_ratio_Neimark_water,marker='o',label='Neimark')
    plt.ylim([-5,0])
    plt.xlabel('lambda')
    plt.ylabel('log10(Dw/DB)')
    plt.legend()

def plot_Nafion():
    log_array_nafion = np.log10(D_ratio_Nafion)
    plt.plot(lam,log_array_nafion,marker='o',label='Nafion')
    #plt.ylim([-5,0])
    plt.xlabel('lambda')
    plt.ylabel('log10(Dn/DB)')
    plt.legend()

#plot_water()
#plot_proton()
plot_Nafion()
plt.show()
