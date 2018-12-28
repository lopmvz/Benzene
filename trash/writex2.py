#!/usr/env python

from sys import argv, stdout

def read_file( fd ):
        lineit = iter(fd)
        E = {}
        f = {}
        sym = {}
        n = {}
        s = 0
        for line in lineit:
                if 'Solving for CVS-EOMEE-CCSD' in line:
                        sym[s] = line.split()[3]
                        for i in range(4):
                            next(lineit)
                        n[s] = int(next(lineit).split()[0])
                        for i in range(4):
                            next(lineit)
                        conv = int(next(lineit).split()[1])
                        while conv != n[s]:
                            curline = next(lineit)
                            conv = int(curline.split()[1])
                            if conv == n[s]:
                                E[s] = {}
                                for i in range(conv):
                                    e = curline.split()[4+i]
                                    e = e[:-1]
                                    E[s][i] = e
                        s += 1
                        #print (E)
                if 'Start computing the transition properties' in line:
                    for n in range(7):
                        next(lineit)              
                    for i in range (len(E)):
                        f[i] = {}
                        for j in range (len(E[i])):
                            #print(i)
                            #print(j)
                            curline = next(lineit)           
                            f[i][j] = curline.split()[3]
                            for m in range(10):
                                next(lineit)                         
                    #print (f)

        for a in range(len(E)):
            #print (sym[a])
            for b in range (len(E[a])):
                print ("&&", sym[a], "&", E[a][b], "&", f[a][b], "\\") 


if __name__ == '__main__':
    with open(argv[1],'r') as fd:
        read_file(fd)
