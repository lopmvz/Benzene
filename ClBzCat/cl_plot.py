import sys
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from scipy.interpolate import interp1d

x1shift = - 1.5 # = 285.4 - 286

#datadummy = np.genfromtxt('dummy.txt')
xdummy = 0 #datadummy[:,0] 
ydummy = 0 #datadummy[:,1]
data1 = np.genfromtxt('clbz_cl_xas_6311_2ppGss_ucC.dat')
stcks1 = np.genfromtxt('clbz_cl_xas_6311_2ppGss_ucC.txt')
ip1 = 207.45
x1 = data1[:,0] 
y1 = data1[:,1]
stcksx1 = stcks1[:,0] 
stcksy1 = stcks1[:,1]

#data2 = np.genfromtxt('b1u.lor')
#stcks2 = np.genfromtxt('b1u.dat')
#x2 = data2[:,0] 
#y2 = data2[:,1]
#stcksx2 = stcks2[:,0] 
#stcksy2 = stcks2[:,1]
#
#data3 = np.genfromtxt('b2u.lor')
#stcks3 = np.genfromtxt('b2u.dat')
#x3 = data3[:,0] 
#y3 = data3[:,1]
#stcksx3 = stcks3[:,0] 
#stcksy3 = stcks3[:,1]
#
#data4 = np.genfromtxt('b3u.lor')
#stcks4 = np.genfromtxt('b3u.dat')
#x4 = data4[:,0] 
#y4 = data4[:,1]
#stcksx4 = stcks4[:,0] 
#stcksy4 = stcks4[:,1]

#Experiment
data10 = np.genfromtxt('Cl_ClBz_exp.csv')
ip10 = 0.0 #aprox
x10 = data10[:,1] 
y10 = (data10[:,0])
#print x10[1]
#f = interp1d(x10, y10, kind='slinear')
#x10new = np.linspace(x10.min(),x10.max(),1000)
#y10new = f(x10new)

data20 = np.genfromtxt('Cl_ClBzCat_exp.csv')
ip20 = 0.0 #aprox
x20 = data20[:,1] 
y20 = (data20[:,0])
#f = interp1d(x20, y20, kind='slinear')
#x20new = np.linspace(x20.min(),x20.max(),1000)
#y20new = f(x20new)

params = {'mathtext.default': 'regular' }          
plt.rcParams.update(params)

f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=False)
plt.xlim(190,207) #
yip = 0.03

#plt.suptitle('C$_6$H$_6$')
plt.xlabel('Excitation energy (eV)')
#ax1.ylim(0.0,0.03)
#ax2.ylim(-0.2,0.03)
plt.ylabel('                                             Intensity (arb. units)')
#plt.yticks([])
ax1.plot([ip1+x1shift,ip1+x1shift],[0,yip],'crimson',linewidth=1.0, dashes=[5, 2])
ax1.plot(x1+x1shift, y1,'crimson', label='ClBz', linewidth=2)
#ax1.plot(x2+x1shift, y2*1, 'darkblue', label='S1($n\pi^*$)  x 10', linewidth=2)
#ax1.plot(x2+x1shift, y2*1, 'darkblue', label='1\B1u', linewidth=2)
#ax1.plot(x3+x1shift, y3*1, 'g', label='S2 ($\pi\pi^*$)  x 10', linewidth=2)
#ax1.plot(x3+x1shift, y3*2, 'g', label='2\B2u + 2\B3u', linewidth=2)
#ax1.plot(x4+x1shift, y4*1, 'g', label='S2 ($\pi\pi^*$)  x 10', linewidth=2)
#ax1.plot(x4+x1shift, y4*1, 'y', label='2\B3u', linewidth=2)
ax1.plot(xdummy, ydummy, 'white',      label='$\Delta x$ = %.2f eV' %x1shift, linewidth=2)
n=len(stcksx1)
for i in range(n):
    ax1.plot([stcksx1[i]+x1shift,stcksx1[i]+x1shift],[0,stcksy1[i]*1],'crimson',linewidth=1.0)
#n=len(stcksx2)
#for i in range(n):
#    ax1.plot([stcksx2[i]+x1shift,stcksx2[i]+x1shift],[0,stcksy2[i]*1],'darkblue',linewidth=1.0)
#n=len(stcksx3)
#for i in range(n):
#    ax1.plot([stcksx3[i]+x1shift,stcksx3[i]+x1shift],[0,stcksy3[i]*2],'green',linewidth=1.0)
#n=len(stcksx4)
#for i in range(n):
#    ax1.plot([stcksx4[i]+x1shift,stcksx4[i]+x1shift],[0,stcksy4[i]*1],'y',linewidth=1.0)
ax1.legend(loc='upper left',fontsize='small')
ax1.text(201.1, 0.025, 'A', fontsize=12)
ax1.text(202.8, 0.011, 'B ', fontsize=12)
#ax1.text(204.3, 0.005, 'C', fontsize=12)
#ax1.text(stcksx1[11]+x1shift-0.1, stcksy1[11]+0.05, 'D', fontsize=12)

#ax2.plot([ip10,ip10],[0,yip],'k',linewidth=1.0, dashes=[5, 2])
ax2.plot(x10, y10, 'k', label='ClBz', linewidth=2)
ax2.plot(x20, y20, 'grey', label='ClBz$^+$', linewidth=2)
ax2.legend(loc='upper left',fontsize='small')

f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

plt.savefig('Cl_ClBz_NEXAFS.pdf')
plt.show()


#yip = yip + 0.02
#
#plt.xlabel('Excitation energy (eV)')
#plt.ylim(0.0,yip)
#plt.ylabel('                                                Intensity (arb. units)')
#plt.yticks([])
#ax1.plot([ip1+x1shift,ip1+x1shift],[0,yip],'crimson',linewidth=1.0, dashes=[5, 2])
#plt.plot(x1+x1shift, y1,'crimson', label='S0', linewidth=2)
#plt.plot(x2+x1shift, y2*10, 'darkblue', label='S1 x 10', linewidth=2)
#plt.plot(x3+x1shift, y3*10, 'g', label='S2 x 10', linewidth=2)
#plt.plot(x4, y4/20, 'k', label='Exp.', linewidth=2)
#
#ax1.plot(xdummy, ydummy, 'white',      label='$\Delta x$ = %.2f eV' %x1shift, linewidth=2)
#ax1.legend(loc='upper left',fontsize='small')
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
