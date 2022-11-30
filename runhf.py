from scipy.optimize import fsolve
import numpy as np
#import case2_h
#import pypower.case39
#import case6_h

_bus_num,_bus_type,_mq,_Tsp,_Top,_phi = 0,1,2,3,4,5
_fbus,_tbus,_l,_d,_lam = 0,1,2,3,4





def getA(case):
    A = np.zeros((numofbus,numofbran))
    branch = case['branch']
    for branch_num in range(A.shape[1]):
        A[int(branch[branch_num,_tbus])-1,branch_num] = 1
        A[int(branch[branch_num,_fbus])-1,branch_num] = -1
    return A

def func(z):
    eqs = []
    phi = []
    ts = []
    mq = []
    for i in range(numofbus):
        phi.append(z[i])
        ts.append(z[i+tsstartnum])
        mq.append(z[i+mstartnum])
        if int(buses[i,_bus_type])==1:
            #print(phi[i],initvalues[i])
            eqs.append(phi[i]-initvalues[i])
        if int(buses[i,_bus_type])==2:
            eqs.append(phi[i]-initvalues[i])
            eqs.append(ts[i]-initvalues[i+tsstartnum])
        if int(buses[i,_bus_type])==3:
            eqs.append(ts[i]-initvalues[i+tsstartnum])
    mq_mat = np.array(mq).reshape((numofbus,1))
    m = np.linalg.pinv(A).dot(mq_mat).reshape((numofbran,))
    for i in range(numofbus):
        eqs.append(phi[i]-(cp*mq[i]*(ts[i]-to[i]))/(1e6))
    for i in range(numofbran):
        fbus = int(branches[i,_fbus]-1)
        tbus = int(branches[i,_tbus]-1)
        lamb = branches[i,_lam]
        L = branches[i,_l]
        #print(lamb,L,cp,m[i])
        #print(ts[fbus],np.e**(-1*lamb*L/(cp*m[i])))
        eqs.append(ts[tbus]-ts[fbus]*(np.e**(-1*lamb*L/(cp*m[i]))))
    eqs.append(sum(mq))
    return np.array(eqs)


#case = case2_h.case2_h()
def runhf(case):
    global buses,branches,numofbus,numofbran,numofvar,phistartnum,tsstartnum,mstartnum,A,cp,to,initvalues
    buses = case['bus']
    branches = case['branch']
    numofbus = buses.shape[0]
    numofbran = branches.shape[0]
    numofvar = numofbus * 3
    phistartnum = 0
    tsstartnum = numofbus * 1
    mstartnum = numofbus * 2
    A = getA(case)
    cp = 4.2e3
    to = buses[:,_Top]
    
    philist = buses[:,_phi]
    tslist = buses[:,_Tsp]
    mlist = buses[:,_mq]
    initvalues = np.hstack((philist,tslist,mlist)).reshape((numofvar,))
    
    res = fsolve(func,initvalues)
    print('func error in heat system:',func(res).sum())
    for i in range(numofbus):
        case['bus'][i,2] = res[mstartnum+i]
        case['bus'][i,3] = res[tsstartnum+i]
        case['bus'][i,5] = res[phistartnum+i]
    return case

'''
if __name__ == '__main__':
    case = case6_h.case6_h()
    res = runhf(case)
    res2 = runhf(res)
'''