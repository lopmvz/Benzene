#!/usr/env python

from sys import argv, stdout
import sys
import numpy as np
from pylab import *

def lorentz(omega, exci, sigma,forza):
    grecopi=3.14159265358979323846264338327950288
    return (sigma*forza)/(grecopi*((omega-exci)**2+sigma**2))

def read_file( fd ):

        data = np.genfromtxt(fd)
        exci_SD1 = data[:,0] 
        fCCSD1 = (data[:,1])
        exci_auSD1=exci_SD1*(1.0/27.2114)

        gamma = 0.4 #eV
        sigma = gamma/2
        n=len(exci_auSD1)
        for i in range(0,n,1):
           fCCSD1[i] = fCCSD1[i]

        step = 0.01
        omega = np.arange(270,300,step) #Bz
        #omega = np.arange(200,210,step) #Cl-Bz
        #omega = np.arange(180,200,step) #Br-Bz
        speCCSD1 = []

        for i in range(0, len(omega), 1):
               speCCSD1.append(0.0)
        for i in range(0, len(exci_SD1), 1):
            for n in range(0, len(omega), 1):
                speCCSD1[n]=speCCSD1[n]+lorentz(omega[n],exci_SD1[i],sigma,fCCSD1[i])

        for i in range(0, len(omega), 1):
            print omega[i], speCCSD1[i]


if __name__ == '__main__':
    with open(argv[1],'r') as fd:
        read_file(fd)

