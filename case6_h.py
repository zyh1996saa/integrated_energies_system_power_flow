import numpy as np

def case6_h():
    
    
    case = {'version':1}
    """
        branch data format
        from_bus_num,to_bus_num,length(m),diameter(mm),lambda(W/mK)#热传导系数
    """
    case['branch'] = np.array([
        [1,2,297.6,125,0.321],
        [2,3,212.5,40,0.21],
        [2,4,301.5,40,0.21],
        [2,5,194.5,100,0.327],
        [5,6,131.3,40,0.189],
    ])
    
    """
        bus_num,bus_type,mq,Tsp,Top,phi(节点编号，节点类型，注入流量 m^3，相对供水温度 ℃，相对回水温度 ℃，热负荷 MW)
    """
    case['bus'] = np.array([
        [1,3,-2,90,40,0],
        [2,1,0.4,90,40,0.1],
        [3,1,0.4,90,40,0.1],
        [4,1,0.4,90,40,0.1],
        [5,1,0.4,90,40,0.1],
        [6,1,0.4,90,40,0.1],
    ])
    
    case['control'] = 'Quantitative'
    return case
