import sys
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.interpolate import spline
from pylab import *
from scipy.interpolate import interp1d

x1shift = 0#- 1.1
x11shift = 0#- 1.1
x2shift = 0#- 1.14
x22shift = 0#- 1.14

data1 = np.genfromtxt('benzene_xas_6311_2ppGss_ucC.dat')
stcks1 = np.genfromtxt('benzene_xas_6311_2ppGss_ucC.txt')
ip1 = 290.9
x1 = data1[:,0] 
y1 = data1[:,1]
stcksx1 = stcks1[:,0] 
stcksy1 = stcks1[:,1]

data11 = np.genfromtxt('bzcat_unrel.txt')
#ip11 = 2911.85
stcksx11 = data11[:,0] 
stcksy11 = (data11[:,1])
data11 = np.genfromtxt('bzcat_unrel.dat')
x11 = data11[:,0] 
y11 = (data11[:,1])

#
data22 = np.genfromtxt('bzcat_rel.txt')
#ip22 = 291.90
stcksx22 = data22[:,0] 
stcksy22 = (data22[:,1])
data22 = np.genfromtxt('bzcat_rel.dat')
x22 = data22[:,0] 
y22 = (data22[:,1])

#Experiment
#data5 = np.genfromtxt('adenine_C_exp.csv')
#ip5 = 291.10
#x5 = data5[:,0] 
#y5 = (data5[:,1])
#x5new = np.linspace(x5.min(),x5.max(),500) #300 represents number of points to make between T.min and T.maxy5new = spline(x5,y5,x5new)f = interp1d(x5, y5, kind='slinear')
#y5new = f(x5new)

params = {'mathtext.default': 'regular' }          
plt.rcParams.update(params)

#f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
#plt.suptitle('C$_6$H$_6^+$')


plt.xlim(280,293) 
yip = 0.5
plt.xlabel('Excitation energy (eV)')
plt.ylabel('                                           Intensity (arb. units)')
plt.ylim(0,yip) 
#plt.yticks([])

#plt.plot(x1+x1shift, y1, 'crimson', label='Non-planar geometry ( %.2f eV)' %x1shift, linewidth=2)#, linestyle='--')
#plt.set_title('Neutral geometry')
plt.plot(x1+x1shift, y1, 'crimson', label='Bz', linewidth=2)#, linestyle='--')
plt.plot(x11+x11shift, y11, 'darkblue', label='Bz$^+$ unrelaxed', linewidth=2)#, linestyle='--')
plt.plot(x22+x22shift, y22, 'green', label='Bz$^+$ relaxed', linewidth=2)#, linestyle='--')
plt.legend(loc='upper right',fontsize='small', framealpha=1)
plt.plot([ip1+x1shift,ip1+x1shift],[0,yip],'crimson',linewidth=1.0, dashes=[5, 2])

n=len(stcksx1)
for i in range(n):
    plt.plot([stcksx1[i]+x1shift,stcksx1[i]+x1shift],[0,stcksy1[i]*1],'crimson',linewidth=1.0)
n=len(stcksx11)
for i in range(n):
    plt.plot([stcksx11[i]+x11shift,stcksx11[i]+x11shift],[0,stcksy11[i]*1],'darkblue',linewidth=1.0)
n=len(stcksx22)
for i in range(n):
    plt.plot([stcksx22[i]+x22shift,stcksx22[i]+x22shift],[0,stcksy22[i]*1],'green',linewidth=1.0)

#ax2.set_title('Cation geometry')
#n=len(stcksx2)
#for i in range(n):
#    ax2.plot([stcksx2[i]+x2shift,stcksx2[i]+x2shift],[0,stcksy2[i]*1],'crimson',linewidth=1.0)

#ax2.plot(x2+x2shift, y2, 'crimson', label='aug-cc-pVDZ', linewidth=2)#, linestyle='--')
#ax2.plot([ip2+x2shift,ip2+x2shift],[0,yip],'darkblue',linewidth=1.0, dashes=[5, 2])
#
#ax2.legend(loc='upper right',fontsize='small', framealpha=1)
#
#
#ax3.plot(x5, y5/4, 'black', label='Experiment' , linewidth=2 )
#ax3.plot([ip5,ip5],[0,yip],'black',linewidth=1.0, dashes=[5, 2])
#ax3.legend(loc='upper right',fontsize='small', framealpha=1)
#
#f.subplots_adjust(hspace=0)
#plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

plt.savefig('BzCat.pdf')
plt.show()
