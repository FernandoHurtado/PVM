#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:19:13 2019

@author: f
"""
from collections import namedtuple
Values = namedtuple('Values','Budget Probability Approval BCS_CG BCS_IG WCS_CG WCS_IG')



class DesicionTheory ():
    def ExpectedValue (BCS, WCS, Probability):
        return ((BCS * Probability)+(WCS * (1 - Probability)))        
    
class Ethics (): 
    def Select (Values, name):
        if (name == "Utilitarianism"):
            return Ethics.Utilitarianism(Values)
        if (name == "Nihilism"):
            return Ethics.Nihilism(Values)
            
    def Utilitarianism (Values):
        # BCS
        value_BC = 0
        value_BC = Values.BCS_IG / 10
        value_BC += Values.Approval / 10
        value_BC += Values.BCS_CG
        # WCS
        value_WC = 0
        value_WC = Values.WCS_IG / 10
        value_WC += Values.Approval / 10
        value_WC += Values.WCS_CG
        
        return value_BC, value_WC
        
    def IdealUtilitarianism (Values):
        # BCS
        value_BC = 0
        value_BC = Values.BCS_IG / 10
        value_BC += Values.Approval / 10
        value_BC += Values.BCS_CG
        # WCS
        value_WC = 0
        value_WC = Values.WCS_IG / 10
        value_WC += Values.Approval / 10
        value_WC += Values.WCS_CG
        value_WC /= 10
        
        return value_BC, value_WC
    
    def Egoism (Values):
        # BCS
        value_BC = 0
        value_BC = Values.BCS_CG / 10
        value_BC += Values.Approval / 10
        value_BC += Values.BCS_IG
        # WCS
        value_WC = 0
        value_WC = Values.WCS_CG / 10
        value_WC += Values.Approval / 10
        value_WC += Values.WCS_IG
        
        return value_BC, value_WC
    
    def LiberalIndividualism (Values):
        # BCS
        value_BC = 0
        
        value_BC = Values.BCS_CG / 2
        value_BC += Values.Approval
        value_BC += Values.BCS_IG
        
        # WCS
        value_WC = 0
        value_WC = Values.WCS_CG / 2
        value_WC += Values.Approval
        value_WC += Values.WCS_IG
        
        return value_BC, value_WC
    
    
    def ConsensusEthics (Values):
        # BCS
        value_BC = 0
        
        value_BC = Values.BCS_CG / 10
        value_BC += Values.BCS_IG / 10
        value_BC += Values.Approval
        
        # WCS
        value_WC = 0
        value_WC = Values.WCS_CG / 10
        value_WC += Values.WCS_IG / 10
        value_WC += Values.Approval
        
        return value_BC, value_WC
    
    def Nihilism (Values):
        return 0, 0
    
    
def main(): # for testing purpouses 
    MedicareForAll = Values(Budget = 20,Probability = 90,Approval = 50,BCS_CG=100,BCS_IG = -20,WCS_CG=50,WCS_IG=-90)    
    Evaluate(MedicareForAll, 'Nihilism')
    
def Evaluate(Values, name):
    
    BCS, WCS = Ethics.Select(Values, name)

    EV = DesicionTheory.ExpectedValue(BCS, WCS, Values.Probability / 100)
    
    if EV > Values.Budget:
        print("law passes")
    else:
        print("law doesn't pass")
        
    print(EV)
         
main()