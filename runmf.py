import numpy as np
import copy 
#import case_IES_14_6_6 as case
import rungf2
import pypower.runpf as runpf
import runhf

def show_pf_res(p_res):
    if p_res[1] == 1:print('power flow converge')
    else:print('power flow not converge')
    return p_res[0]
        

def runmf(case):
    """
        run power flow of multiple energies system 
    """
    
    # case re-build
    g_case = {'branch':case['branch_g'],'bus':case['bus_g']}
    h_case = {'branch':case['branch_h'],'bus':case['bus_h']}
    p_case = {'branch':case['branch_p'],'bus':case['bus_p'],'gen':case['gen'],'gencost':case['gencost'],'baseMVA':case['baseMVA'],'version':'2'}
    
    g_res = rungf2.rungf(g_case)
    h_res = runhf.runhf(h_case)
    p_res = runpf.runpf(p_case)
    p_res = show_pf_res(p_res)
        
    ncase = copy.deepcopy(case)
    ncase['branch_g'] = g_res['branch']
    ncase['bus_g'] = g_res['bus']
    ncase['branch_h'] = h_res['branch']
    ncase['bus_h'] = h_res['bus']
    ncase['branch_p'] = p_res['branch']
    ncase['bus_p'] = p_res['bus']
    
    return ncase

'''
if __name__ == "__main__":
    ies_case = case.case_14_6_6()
    res = runmf(ies_case)'''