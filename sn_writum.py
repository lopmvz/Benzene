#!/usr/env python

from sys import argv, stdout

def read_file( fd ):
        lineit = iter(fd)
        E_State_A = 6.27
        string = 'State A: eomee_ccsd/rhfref/singlets: 1/A1'
        E0 = {}
        sym0 = {}
        n0 = {}
        s0 = 0

        E = {}
        En = {}
        E2 = {}
        f = {}
        f1 = {}
        f2 = {}
        if1 = 0
        jf1 = 0
        sym = {}
        n = {}
        s = 0
        ios = 0
        ios1 = 0
        ios2 = 0
        si = 0
        for line in lineit:
                if 'Solving for EOMEE-CCSD' in line:
                        sym0[s0] = line.split()[3]
                if '   EOMEE-CCSD/MP2 right amplitudes will be solved using Davidson' in line:
                        for i in range(3):
                            curline = next(lineit)
                            if 'LinDepThresh=1.00e-15' in curline:
                                for j in range(3):
                                    curline = next(lineit)
                        print(curline)
                        n0[s0] = int(curline.split()[0])
                        for i in range(4):
                            next(lineit)
                        conv = int(next(lineit).split()[1])
                        while conv != n0[s0]:
                            curline = next(lineit)
                            if 'complex' in curline :
                                curline = next(lineit)
                            conv = int(curline.split()[1])
                            if conv == n0[s0]:
                                E0[s0] = {}
                                for i in range(conv):
                                    e = curline.split()[4+i]
                                    e = e[:-1]
                                    E0[s0][i] = e
                        f0[s0] = {}
                        s0 += 1
                if 'Solving for CVS-EOMEE-CCSD' in line:
                        sym[s] = line.split()[3]

                if 'CVS-EOMEE-CCSD/MP2 right amplitudes will be solved using Davidson' in line:

                        for ii in range(3):
                            curline = next(lineit)
                            if 'LinDepThresh=1.00e-15' in curline:
                                for jj in range(3):
                                    curline = next(lineit)
                        n[s] = int(curline.split()[0])
                        #print (n[s])
                        for i in range(4):
                            next(lineit)
                        conv = int(next(lineit).split()[1])
                        while conv != n[s]:
                            curline = next(lineit)
                            if 'complex' in curline :
                                curline = next(lineit)
                            conv = int(curline.split()[1])
                            if conv == n[s]:
                                E[s] = {}
                                En[s] = {}
                                for i in range(conv):
                                    e = curline.split()[4+i]
                                    e = e[:-1]
                                    E[s][i] = e
                                    En[s][i] = float(e) 
                        f[s] = {}

                        s += 1
                if string in line:
                        StateA = line.split()[-1]
                        for i in range(1):
                                curline = next(lineit)
                        StateB_flag = (curline).split()[2]
                        StateB = (curline).split()[-1]
                        if (StateB_flag == "cvs_eomee_ccsd/rhfref/singlets:"):
                            for i in range(4):
                                curline = next(lineit)
                            f[si][ios] = float(curline.split()[3])
                            #if f[si][ios] > 0:
                                #print("&", StateB[2:], "&", "{0:.2f}".format(En[si][ios]-E_State_A), "&", "{0:.6f}".format(float(curline.split()[3])), "\\"+"\\")
                            print("{0:.4f}".format(En[si][ios]-E_State_A), "{0:.6f}".format(float(curline.split()[3])))
                            if (ios < len(En[si])-1):
                                ios=ios+1
                            else:
                                ios=0
                                si+=1

if __name__ == '__main__':
    with open(argv[1],'r') as fd:
        read_file(fd)
