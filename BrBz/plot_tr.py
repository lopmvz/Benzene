import sys
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from scipy.interpolate import interp1d

x1shift = - 1.80 # 

#datadummy = np.genfromtxt('dummy.txt')
xdummy = 0 #datadummy[:,0] 
ydummy = 0 #datadummy[:,1]

data1 = np.genfromtxt('brbz_xas_6311_2ppGss_ucC.dat')
stcks1 = np.genfromtxt('brbz_xas_6311_2ppGss_ucC.txt')
ip1 = 290.9
x1 = data1[:,0] 
y1 = data1[:,1]
stcksx1 = stcks1[:,0] 
stcksy1 = stcks1[:,1]

data2 = np.genfromtxt('b1.dat')
stcks2 = np.genfromtxt('b1.txt')
x2 = data2[:,0] 
y2 = data2[:,1]
stcksx2 = stcks2[:,0] 
stcksy2 = stcks2[:,1]

data3 = np.genfromtxt('b2.dat')
stcks3 = np.genfromtxt('b2.txt')
x3 = data3[:,0] 
y3 = data3[:,1]
stcksx3 = stcks3[:,0] 
stcksy3 = stcks3[:,1]

data4 = np.genfromtxt('a1.dat')
stcks4 = np.genfromtxt('a1.txt')
x4 = data4[:,0] 
y4 = data4[:,1]
stcksx4 = stcks4[:,0] 
stcksy4 = stcks4[:,1]

#Experiment


plt.xlim(278,291.1) #
yip = 0.12


plt.xlabel('Excitation energy (eV)')
plt.ylim(0.0,yip)
plt.ylabel('Intensity (arb. units)')
plt.yticks([])
plt.plot([ip1+x1shift,ip1+x1shift],[0,yip],'crimson',linewidth=1.0, dashes=[5, 2])
plt.plot(x1+x1shift, y1,'crimson', label='S$_0$', linewidth=2)
#plt.plot(x2+x1shift, y2*1, 'darkblue', label='S1($n\pi^*$)  x 10', linewidth=2)
plt.plot(x2+x1shift, y2*1, 'darkblue', label='1\B$_{1}$', linewidth=2)
#plt.plot(x3+x1shift, y3*1, 'g', label='S2 ($\pi\pi^*$)  x 10', linewidth=2)
plt.plot(x3+x1shift, y3*1, 'g', label='1\B$_{2}$', linewidth=2)
#plt.plot(x4+x1shift, y4*1, 'g', label='S2 ($\pi\pi^*$)  x 10', linewidth=2)
plt.plot(x4+x1shift, y4*1, 'y', label='1\A$_{1}$', linewidth=2)
plt.plot(xdummy, ydummy, 'white',      label='$\Delta$x = %.2f eV' %x1shift, linewidth=2)
n=len(stcksx1)
for i in range(n):
    plt.plot([stcksx1[i]+x1shift,stcksx1[i]+x1shift],[0,stcksy1[i]*1],'crimson',linewidth=1.0)
n=len(stcksx2)
for i in range(n):
    plt.plot([stcksx2[i]+x1shift,stcksx2[i]+x1shift],[0,stcksy2[i]*1],'darkblue',linewidth=1.0)
n=len(stcksx3)
for i in range(n):
    plt.plot([stcksx3[i]+x1shift,stcksx3[i]+x1shift],[0,stcksy3[i]*1],'green',linewidth=1.0)
#n=len(stcksx4)
#for i in range(n):
#    plt.plot([stcksx4[i]+x1shift,stcksx4[i]+x1shift],[0,stcksy4[i]*1],'y',linewidth=1.0)
plt.legend(loc='upper left',fontsize='small')


plt.savefig('BrBz_TRNEXAFS.pdf')
plt.show()


#yip = yip + 0.02
#
#plt.xlabel('Excitation energy (eV)')
#plt.ylim(0.0,yip)
#plt.ylabel('                                                Intensity (arb. units)')
#plt.yticks([])
#plt.plot([ip1+x1shift,ip1+x1shift],[0,yip],'crimson',linewidth=1.0, dashes=[5, 2])
#plt.plot(x1+x1shift, y1,'crimson', label='S0', linewidth=2)
#plt.plot(x2+x1shift, y2*10, 'darkblue', label='S1 x 10', linewidth=2)
#plt.plot(x3+x1shift, y3*10, 'g', label='S2 x 10', linewidth=2)
#plt.plot(x4, y4/20, 'k', label='Exp.', linewidth=2)
#
#plt.plot(xdummy, ydummy, 'white',      label='$\Delta x$ = %.2f eV' %x1shift, linewidth=2)
#plt.legend(loc='upper left',fontsize='small')
#
#
#ax2.plot(x1+x1shift, y1,'crimson', label = 'S0 ($\Delta x$ = %.2f eV)' %x1shift, linewidth=2)
#ax2.plot([ip1+x1shift,ip1+x1shift],[0,yip],'crimson',linewidth=1.0, dashes=[5, 2])
#n=len(stcksx1)
#for i in range(n):
#    ax2.plot([stcksx1[i]+x1shift,stcksx1[i]+x1shift],[0,stcksy1[i]*1],'crimson',linewidth=1.0)
##plt.plot([ip,ip],[0,yip],'k',linewidth=1.0, dashes=[5, 2])
#ax2.plot(x4, y4/20+0.02, 'k', label='S0 Exp.', linewidth=2)
#ax2.legend(loc='upper left',fontsize='small')
#
#f.subplots_adjust(hspace=0)
#plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
#
#plt.savefig('Uracil_Sn_C_1.pdf')
#plt.show()
#
#
#
