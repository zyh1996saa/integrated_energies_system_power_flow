import numpy as np

def case11_g():
    
    
    case = {'version':1}
    """
        branch data format
        from_bus_num,to_bus_num,length(m),diameter(mm),
    """
    case['branch'] = np.array([
        [1,2,50,160],
        [2,3,500,160],
        [2,4,500,110],
        [2,5,600,110],
        [3,6,600,110],
        [3,7,600,110],
        [3,8,500,110],
        [5,6,600,80],
        [4,7,600,80],
        [6,8,780,80],
        [7,8,780,80],
        [7,9,200,80],
        [9,10,200,80],
        [10,11,200,80],
    ])
    
    """
        bus_num,bus_type,load(m^3/s),presure(pa)(节点编号，节点类型，注入流量，压力)
    """
    case['bus'] = np.array([
        [1,3,-1339.2,7.5],
        [2,1,350,6.6],
        [3,1,203,4.67],
        [4,1,166,4.70],
        [5,1,188,4.145],
        [6,1,128,3.84],
        [7,1,45,3.93],
        [8,1,165,3.74],
        [9,1,42,2.82],
        [10,1,28,2.414],
        [11,1,19,2.342],
    ])

    case['constant'] = 0.25959700349209436

    return case

def getA(case):
    A = np.zeros((numofbus,numofbran))
    branch = case['branch']
    for branch_num in range(A.shape[1]):
        A[int(branch[branch_num,_tbus])-1,branch_num] = 1
        A[int(branch[branch_num,_fbus])-1,branch_num] = -1
    return A

if __name__ == "__main__": 
    _fbus,_tbus,_l,_d = 0,1,2,3
    case = case11_g()
    
    buses = case['bus']
    branches = case['branch']
    numofbus = buses.shape[0]
    numofbran = branches.shape[0]
    A = getA(case)
    np.linalg.pinv(A).dot(case['bus'][:,2].reshape(11,1))