from sys import argv, stdout

def read_file( fd ):
    s0 = 0
    sym0 = {}
    n0 = {}
    E0 = {}
    sn = 0
    nn = {}
    En = {}
    fn = {}
    cnsym = 0
    cnstt = 0
    lineit = iter(fd)
    for line in lineit:
        if 'Solving for EOMEE-CCSD' in line:
            s0 += 1
            sym0[s0-1] = line.split()[3]
        if '   EOMEE-CCSD/MP2 right amplitudes will be solved using Davidson' in line:
            for i in range(3):
                curline = next(lineit)
                if 'LinDepThresh=1.00e-15' in curline:
                    for j in range(3):
                        curline = next(lineit)
                    n0[s0-1] = int(curline.split()[0])
                    for i in range(4):
                        next(lineit)
                    conv = int(next(lineit).split()[1])
                    while conv != n0[s0-1]:
                        curline = next(lineit)
                        if 'complex' in curline :
                            curline = next(lineit)
                        conv = int(curline.split()[1])
                        if conv == n0[s0-1]:
                            E0[s0-1] = {}
                            for i in range(conv):
                                e = curline.split()[4+i]
                                e = e[:-1]
                                E0[s0-1][i] = e

        if 'CVS-EOMEE-CCSD/MP2 right amplitudes will be solved using Davidson' in line:
            sn += 1
            for i in range(3):
                curline = next(lineit)
                if 'LinDepThresh=1.00e-15' in curline:
                    for j in range(3):
                        curline = next(lineit)
                    nn[sn-1] = int(curline.split()[0])
                    for i in range(4):
                        next(lineit)
                    conv = int(next(lineit).split()[1])
                    while conv != nn[sn-1]:
                        curline = next(lineit)
                        if 'complex' in curline :
                            curline = next(lineit)
                        conv = int(curline.split()[1])
                        if conv == nn[sn-1]:
                            En[sn-1] = {}
                            fn[sn-1] = {}
                            for i in range(conv):
                                e = curline.split()[4+i]
                                e = e[:-1]
                                En[sn-1][i] = e

            nsym = len(En)
            nstt = len(En[cnsym])
            #fn[0] = {}
#    print(len(E0)
#        print(len(En[cnsym]))
    #lineit = iter(fd)
    #for line in lineit:
        if 'State A: eomee_ccsd/rhfref/singlets:' in line:
            if 'State B: cvs_eomee_ccsd/rhfref/singlets: ' in next(lineit):
                print("Sym: ",next(lineit).split()[-1])
                for i in range(3):
                    curline = next(lineit)
                    #if (i==0):
                #if (cnstt < len(E1[0])):
                fn[cnsym][cnstt] = float(curline.split()[3])
                if (cnstt < nstt -1 ):
                    cnstt += 1
                    #print(cnstt)
                elif (cnsym < nsym):
                    fn[cnsym] = {}   
                    cnsym += 1
                    nstt = len(En[cnsym])
                    cnstt = 0
        #print(cnsym) 
        #print(cnstt) 
        #print(fn)


 #                   ios1+=1
 #               elif (ios < ( len(E1[1]) + len(E1[0]) ) ):
 #                   f1[1][ios11] = float(curline.split()[3])
 #                   ios11+=1  
 #               ios+=1    

        #if 'Solving for CVS-EOMEE-CCSD' in line:
        #    Sym0 = line.split()[3]


#        if 'Point group:' in line:
#            dummy = line.split()[3]
#            ir = float(dummy[-1:]) #irreducible representation
#            Eval = [ir]
#            fval = [ir]
#            
#            Ecvs = [ir]
#            fcvs = [ir]



#
# #           for j in range(len(En)):
#  #              E1[j] = {}
#   #             f1[j] = {}
#    #            for k in range(len(En[j])):
#     #               E1[j][k] =  float(En[j][k]) - float(E0[0][0])
#      #              f1[j][k] =  0.0
#    
#            for j in range(len(En)):
#                E2[j] = {}
#                f2[j] = {}
#                for k in range(len(En[j])):
#                    E2[j][k] = float(En[j][k]) - float(E0[0][0]) 
#                    f2[j][k] = 0.0 
#
#
#        if 'State A: eomee_ccsd/rhfref/singlets: 1/A"' in line:
#            if 'State B: cvs_eomee_ccsd/rhfref/singlets: ' in next(lineit):
#                for i in range(4):
#                    curline = next(lineit)
#                if (ios2 < (len(E2[0]) )):
#                    f2[0][ios2] = float(curline.split()[3])
#                elif (ios2 < ( len(E2[1]) + len(E2[0]) ) ):
#                    f2[1][ios22] = float(curline.split()[3])
#                    ios22+=1  
#                ios2+=1  
#
# #   print(E1)
#  #  print(E2)
# #   print("S2")
#  #  for a in range(len(E1)):
#   #     for b in range (len(E1[a])):
#    #        print (E1[a][b],  f1[a][b]) 
#
#    print("S1")
#    for a in range(len(E2)):
#        if (a == 0):
#            sym = "A'"
#        else:
#            sym = "A\""
#        for b in range (len(E2[a])):
#            print ("&", sym, "&", "{0:.2f}".format(E2[a][b]), "&",  "{0:.5f}".format(f2[a][b]))
#    sn = 0
#    nn = {}
#    En = {}
#    E1 = {}
#    f1 = {}
#    E2 = {}
#    f2 = {}
#    ios = 0
#    ios1 = 0
#    ios11 = 0    
#    ios2 = 0
#    ios22 = 0
#    lineit = iter(fd)
#    for line in lineit:

if __name__ == '__main__':
    with open(argv[1],'r') as fd:
        read_file(fd)
