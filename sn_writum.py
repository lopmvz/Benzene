#!/usr/env python

from sys import argv, stdout

def read_file( fd ):
        lineit = iter(fd)
        E0 = {}
        f0 = {}
        if10 = 0
        jf10 = 0
        sym0 = {}
        n0 = {}
        s0 = 0
        E = {}
        E1 = {}
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
        for line in lineit:
                if 'Solving for EOMEE-CCSD' in line:
                        sym0[s0] = line.split()[3]
                if '   EOMEE-CCSD/MP2 right amplitudes will be solved using Davidson' in line:
                        for i in range(3):
                            curline = next(lineit)
                            if 'LinDepThresh=1.00e-15' in curline:
                                for j in range(3):
                                    curline = next(lineit)
                        n0[s0] = int(curline.split()[0])
                        #print (n[s])
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
                                E1[s] = {}
                                E2[s] = {}
                                for i in range(conv):
                                    e = curline.split()[4+i]
                                    e = e[:-1]
                                    E[s][i] = e
                                    E1[s][i] = float(e) - float(E0[0][0])
                                    E2[s][i] = float(e) - float(E0[0][1])
                        f[s] = {}
                        f1[s] = {}
                        f2[s] = {}
                        f2[0][0]=0
                        s += 1
                si = 0
                if 'State A:' in line:
                	StateA = line.split()[2]
                	if (StateA == "eomee_ccsd/rhfref/singlets:"):
                	    StateB = next(lineit).split()[2]
                	    if (StateB == "cvs_eomee_ccsd/rhfref/singlets:"):
                	        for i in range(4):
                	        	curline = next(lineit)
                	        #print(curline)
                	        if (ios < len(E1[0])):
                	        	f1[si][ios1] = float(curline.split()[3])
                	        	ios1=ios1+1
                	        elif (ios < len(E1[0])+len(E2[0])):
                	        	ios2+=1
                	        	f2[si][ios2] = float(curline.split()[3])
                	        ios=ios+1

        print("S1")
        for a in range(len(E1)):
            for b in range (len(E1[a])):
                print (E1[a][b],  f1[a][b]) 
        print("S2")
        for a in range(len(E2)):
            for b in range (len(E2[a])):
                print (E2[a][b],  f2[a][b]) 


if __name__ == '__main__':
    with open(argv[1],'r') as fd:
        read_file(fd)
