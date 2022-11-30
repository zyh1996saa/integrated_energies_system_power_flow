import numpy as np
import rungf2 

def case6_g():
    
    
    case = {'version':1}
    """
        branch data format
        from_bus_num,to_bus_num,length(m),diameter(mm), or beta (${m^3}*{s^-1}/Mpa$)
    """
    case['branch'] = np.array([
        [1,3,0.2059/3600],
        [3,5,0.208/3600],
        [3,4,0.1541/3600],
        [2,4,0.1862/3600],
        [4,6,0.1788/3600],
    
    ])
    
    """
        bus_num,bus_type,load(m^3/s),presure(Mpa)(节点编号，节点类型，注入流量，压力)
    """
    case['bus'] = np.array([
        [1,3,0 ,3.1005],
        [2,1,-15.7317,2.7436],
        [3,1,26.571  ,2.82214],
        [4,1,0       ,2.72706],
        [5,1,15.7317 ,2.80905],
        [6,1,46.868  ,2.55826],
        
    ])

    case['constant'] = 0.25959700349209436
    case['pipe_para'] = 'beta'

    return case

rungf2.rungf(case6_g())