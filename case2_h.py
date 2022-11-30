import numpy as np
l = 300
lamb = 0.3
cp = 4.2e3
m = 1
ts1 = 90
ts2 = 90*(np.e**(-1*lamb*l/(cp*m)))
mq1 = -1
mq2 = 1
phi2 = (cp*mq2*(ts2-40))/(1e6)
phi1 = (cp*mq1*(ts1-40))/(1e6)

def case2_h():
    
    
    case = {'version':1}
    """
        branch data format
        from_bus_num,to_bus_num,length(m),diameter(mm),lambda(W/mK)#热传导系数
    """
    case['branch'] = np.array([
        [1,2,300,125,0.3],

    ])
    
    """
        bus_num,bus_type,mq,Tsp,Top,phi(节点编号，节点类型，注入流量，相对供水温度，相对回水温度，热负荷)
    """
    case['bus'] = np.array([
        [1,3,-1,90,40,phi1],
        [2,1,1,ts2,40,phi2],

    ])
    
    case['control'] = 'Quantitative'
    return case