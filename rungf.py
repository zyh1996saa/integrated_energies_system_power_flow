from scipy.optimize import fsolve
import numpy as np
import case2_g 
import case11_g
import copy
_bus_num,_bus_type,_f,_p = 0,1,2,3
_fbus,_tbus,_l,_d = 0,1,2,3


def getA(case):
    A = np.zeros((numofbus,numofbran))
    branch = case['branch']
    for branch_num in range(A.shape[1]):
        A[int(branch[branch_num,_tbus])-1,branch_num] = 1
        A[int(branch[branch_num,_fbus])-1,branch_num] = -1
    return A

def func(z):
    eqs = []
    p = []
    f = []
    for i in range(numofbus):
        p.append(z[i+pstartnum])
        f.append(z[i+fstartnum])
        if int(buses[i,_bus_type])==1:
            eqs.append(f[i]-initvalues[i+fstartnum])
            #print(f[i],initvalues[i+fstartnum])
        if int(buses[i,_bus_type])==3:
            eqs.append(p[i]-initvalues[i+pstartnum])
    dp = np.array([((p[branches[i,0]-1])**2-(p[branches[i,1]-1])**2) for i in range(numofbran) ]).reshape(numofbran,)

    s = np.zeros((numofbran,))
    for i in range(numofbran):
        if p[branches[i,0]-1]**2>=p[branches[i,1]-1]**2:
            s[i] = 1
        else:
            s[i] = -1
    #print(p)
    #print(s)
    #print('-'*20)    
    
    
    fbran = (clist.reshape(numofbran,))*s*np.sqrt(s*dp)
    #print(np.matmul(A,fbran.reshape(numofbran,1)).reshape(numofbus,))
    delta_p = np.matmul(A,fbran.reshape(numofbran,1)).reshape(numofbus,)-np.array(f).reshape(numofbus,)
    #print('A*f_ij:',np.matmul(A,fbran.reshape(numofbran,1)).reshape(numofbus,))
    #print('f:',np.array(f).reshape(numofbus,))
    #print(np.vstack((delta_p.reshape(numofbus,1),np.array(eqs).reshape(numofbus,1))).reshape(numofvar,))
    
    return np.vstack((delta_p.reshape(numofbus,1),np.array(eqs).reshape(numofbus,1))).reshape(numofvar,)


def rungf(case):


    global buses,branches,numofbus,numofbran,numofvar,pstartnum,fstartnum,A,cp,to,initvalues,clist
    buses = case['bus']
    branches = case['branch']
    numofbus = buses.shape[0]
    numofbran = branches.shape[0]
    numofvar = numofbus * 2
    pstartnum = 0
    fstartnum = numofbus * 1
    A = getA(case)
    for i in range(numofbus):
        if int(buses[i,1]) == 3:
            slack_bus_num = i
    del i
    A1 = np.delete(A,[slack_bus_num],axis=0)
    
    clist = np.array([case['constant']*((branches[i,_d]/1000)**2.5)/(branches[i,_l]**0.5) for i in range(numofbran)]).reshape(numofbran,1)
    plist = buses[:,_p]*1e6
    flist = buses[:,_f]
    
    initvalues = np.hstack((plist,flist)).reshape((numofvar,))
    
    res = fsolve(func,initvalues)
    #print(res)
    res[pstartnum:pstartnum+numofbus] = np.abs(res[pstartnum:pstartnum+numofbus])
    print(func(res))
    ncase = copy.deepcopy(case)
    ncase['bus'][:,_f] = res[fstartnum:fstartnum+numofbus].reshape(numofbus,)
    ncase['bus'][:,_p] = res[pstartnum:pstartnum+numofbus].reshape(numofbus,)/1e6
    return case

if __name__ == "__main__":
    #case1 = case2_g.case2_g()
    #res1 = rungf(case1)
    case2 = case11_g.case11_g()
    res2 = rungf(case2)