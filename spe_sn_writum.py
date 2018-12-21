#!/usr/env python

from sys import argv, stdout

def read_file( fd ):
        lineit = iter(fd)
        E0 = {}
        sym0 = {}
        n0 = {}
        s0 = 0
        Eex = {}
        sym = {}
        n = {}
        s = 0
        f_os = {}
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
                        for i in range(4):
                            next(lineit)
                        conv = int(next(lineit).split()[1])
                        while conv != n[s]:
                            curline = next(lineit)
                            if 'complex' in curline :
                            	curline = next(lineit)
                            conv = int(curline.split()[1])
                            if conv == n[s]:
                                Eex[s] = {}
                                f_os[s] = {}
                                for i in range(conv):
                                    e = curline.split()[4+i]
                                    e = e[:-1]
                                    Eex[s][i] = {}
                                    f_os[s][i] = {}
                                    for p0 in range(len(sym0)):
                                        Eex[s][i][p0] = {}
                                        f_os[s][i][p0] = {}
                                        for j0 in range(n0[p0]):
                                            Eex[s][i][p0][j0] = float(e) - float(E0[p0][j0])
                                            f_os[s][i][p0][j0] = 0
                        s += 1

                if 'State A: eomee_ccsd/rhfref/singlets: 1/B1u' in line:
                        StateA = line.split()[2]
                        if (StateA == "eomee_ccsd/rhfref/singlets:"):
                            templine2 = line.split()[3]
                            refsym0 = templine2.split('/')[1]
                            j0 = int(templine2.split('/')[0]) - 1
                            p0 = 0
                            while sym0[p0] != refsym0:
                                p0 += 1
                            templine = next(lineit)
                            StateB = templine.split()[2]
                            if (StateB == "cvs_eomee_ccsd/rhfref/singlets:"):
                                templine2 = templine.split()[3]
                                refsym = templine2.split('/')[1]
                                j = int(templine2.split('/')[0]) - 1
                                p = 0
                                while sym[p] != refsym:
                                    p += 1
                                for i in range(4):
                                        curline = next(lineit)
                                f_os[p][j][p0][j0] = float(curline.split()[3])


        for a in range(len(sym0)):
            for b in range(n0[a]):
                print('%d/%s'%(b+1, sym0[a]))
                for c in range(len(sym)):
                    for d in range(n[c]):
                        print('%d/%s->%d/%s: %feV, f=%f'%(b+1,sym0[a],d+1,sym[c],Eex[c][d][a][b],f_os[c][d][a][b]))

        fin = 0
        for c in range(len(sym)):
            for d in range(n[c]):
                fin += 1

        tempE = [[] for a in range(len(sym0))]
        tempF = [[] for a in range(len(sym0))]

        orderE = [[] for a in range(len(sym0))]
        orderF = [[] for a in range(len(sym0))]

        for a in range(len(sym0)):
            tempE[a] = [[] for b in range(n0[a])]
            tempF[a] = [[] for b in range(n0[a])]
            orderE[a] = [[] for b in range(n0[a])]
            orderF[a] = [[] for b in range(n0[a])]
            for b in range(n0[a]):
                for c in range(len(sym)):
                    for d in range(n[c]):
                        tempE[a][b].append(Eex[c][d][a][b])
                        tempF[a][b].append(f_os[c][d][a][b])

        for a in range(len(sym0)):
            for b in range(n0[a]):
                for t in range(fin):
                   minE = min(tempE[a][b])
                   orderE[a][b].append(minE)
                   indE = tempE[a][b].index(minE)
                   orderF[a][b].append(tempF[a][b][indE])
                   tempE[a][b].pop(indE)
                   tempF[a][b].pop(indE)

        for a in range(len(sym0)):
            for b in range(n0[a]):
                print('%d/%s'%(b+1, sym0[a]))
                for t in range(fin):
                   print('%feV, f=%f'%(orderE[a][b][t],orderF[a][b][t]))


if __name__ == '__main__':
    with open(argv[1],'r') as fd:
        read_file(fd)
