import numpy as np



def case2_g():
    
    
    case = {'version':1}
    """
        branch data format
        from_bus_num,to_bus_num,length(m),diameter(mm),
    """
    case['branch'] = np.array([
        [1,2,50,160],

    ])
    
    """
        bus_num,bus_type,load(m^3/h),presure(Mpa)(节点编号，节点类型，注入流量，压力)
    """
    case['bus'] = np.array([
        [1,3,-1339.2,7.5],
        [2,1,1339.2,6.2],

    ])
    
    #case['constant'] = 0.25959700349209436
    case['constant'] = 0.4
    'k = c*d**2.5/(l**0.5)'    

    return case

