#!/usr/env python

from sys import argv, stdout

def read_file( fd ):
        lineit = iter(fd)
        E = {}
        f = {}
        if1 = 0
        jf1 = 0
        sym = {}
        n = {}
        s = 0
        for line in lineit:
                if 'Solving for CVS-EOMEE-CCSD' in line:
                        sym[s] = line.split()[3]
                        #print (sym[s])
                if 'CVS-EOMEE-CCSD/MP2 right amplitudes will be solved using Davidson' in line:
                        for i in range(3):
                            curline = next(lineit)
                            if 'LinDepThresh=1.00e-15' in curline:
                                for j in range(3):
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
                                for i in range(conv):
                                    e = curline.split()[4+i]
                                    e = e[:-1]
                                    E[s][i] = float(e)
                        f[s] = {}
                        s += 1
                        #print (E)
                if 'Oscillator strength' in line:
                    f[if1][jf1] = float(line.split()[3])
                    if (jf1 != len(E[if1])-1):
                      jf1 += 1
                    else:
                      jf1 = 0
                      if1 += 1
        for a in range(len(E)):
            #print (sym[a])
            for b in range (len(E[a])):
                print ("&", sym[a], "&", "{0:.2f}".format(E[a][b]), "&", "{0:.5f}".format(f[a][b],5), "\\"+"\\") 


if __name__ == '__main__':
    with open(argv[1],'r') as fd:
        read_file(fd)
