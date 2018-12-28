#!/usr/env python

from sys import argv, stdout
import math


if __name__ == '__main__':

    E1 = {}
    f1 = {}
    sym1 = {}
    E2 = {}
    f2 = {}
    sym2 = {}
        
    #with open("benzene_xas_cat_6311_2pp_gss_uc.inp.out",'r') as fd:
    with open("CH2CHF_ee_Pbs.out",'r') as fd:
        n = {}
        s = 0
        lineit = iter(fd)
        for line in lineit:
                if 'Solving for CVS-EOMEE-CCSD' in line:
                        sym1[s] = line.split()[3]
                        for i in range(4):
                            next(lineit)
                        n[s] = int(next(lineit).split()[0])
                        for i in range(4):
                            next(lineit)
                        conv = int(next(lineit).split()[1])
                        while conv != n[s]:
                            curline = next(lineit)
                            if 'complex' in curline:
                                print("hi")
                            else:
                            #    tmpconv = curline.split()[1]
                                conv = int(curline.split()[1])
                                if conv == n[s]:
                                    E1[s] = {}
                                    for i in range(conv):
                                        e = curline.split()[4+i]
                                        e = e[:-1]
                                        E1[s][i] = float(e)
                        s += 1
                if 'Start computing the transition properties' in line:
                    for n in range(7):
                        next(lineit)              
                    for i in range (len(E1)):
                        f1[i] = {}
                        for j in range (len(E1[i])):
                            curline = next(lineit)           
                            f1[i][j] = float(curline.split()[3])
                            for m in range(10):
                                next(lineit) 

    with open("H2O_exc_Dbs.out",'r') as fd:
        lineit = iter(fd)
        n = {}
        s = 0
        for line in lineit:
                if 'Solving for CVS-EOMEE-CCSD' in line:
                        sym2[s] = line.split()[3]
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
                                E2[s] = {}
                                for i in range(conv):
                                    e = curline.split()[4+i]
                                    e = e[:-1]
                                    E2[s][i] = float(e)
                        s += 1
                        #print (E)
                if 'Start computing the transition properties' in line:
                    for n in range(7):
                        next(lineit)              
                    for i in range (len(E2)):
                        f2[i] = {}
                        for j in range (len(E2[i])):
                            #print(i)
                            #print(j)
                            curline = next(lineit)           
                            f2[i][j] = float(curline.split()[3])
                            for m in range(10):
                                next(lineit)     
                    #print (f)
        
        for a in range(len(E1)):
            #print (sym[a])
            for b in range (len(E1[a])):
#                print ("&", sym1[a][0]+ "$_"+ sym1[a][1]+"$","&", "{0:.2f}".format(E1[a][b]),"&", "{0:.4f}".format(f1[a][b],4), 
#                    "&", sym2[a][0]+ "$_"+ sym2[a][1]+"$","&", "{0:.2f}".format(E2[a][b]), "&", "{0:.4f}".format(f2[a][b],4), "\\"+"\\") 
                print ("&", sym1[a],"&", "{0:.2f}".format(E1[a][b]),"&", "{0:.4f}".format(f1[a][b],4), 
                    "&", sym2[a],"&", "{0:.2f}".format(E2[a][b]), "&", "{0:.4f}".format(f2[a][b],4), "\\"+"\\") 
#                print ("&", sym1[a][0]+ "$_"+ sym1[a][1]+"$"+ sym1[a][2],"&", "{0:.2f}".format(E1[a][b]),"&", "{0:.4f}".format(f1[a][b],4), 
#                    "&", sym2[a][0]+ "$_"+ sym2[a][1]+"$","&", "{0:.2f}".format(E2[a][b]), "&", "{0:.4f}".format(f2[a][b],4), "\\"+"\\") 






