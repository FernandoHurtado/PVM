#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:19:13 2019

@author: f
"""
from collections import namedtuple
Values = namedtuple('Budget','Probability','Approval','BCS_CG','BCS_IG', 'WCS_CG', 'WCS_IG')
MedicareForAll = Values(Budget = 20,Probability = 90,Approval = 50,BCS_CG=100,BCS_IG = -20,WCS_CG=50,WCS_IG=-90)



class DesicionTheory ():
    def ExpectedValue (BCS, WCS, Probability):
        return ((BCS * Probability)+(WCS * (1 - Probability)))        
    
class Ethics (): 
    def Select (Values, name):
        if (name == "Utilitarianism"):
            return Ethics.Utilitarianism(Values)
            
    def Utilitarianism (Values):
        # BCS
        value_BC = 0
        value_BC = Values.BC_IG / 10
        value_BC += Values.Approval / 10
        value_BC += Values.BC_CG
        # WCS
        value_WC = 0
        value_WC = Values.WC_IG / 10
        value_WC += Values.Approval / 10
        value_WC += Values.WC_CG
        
        return value_BC, value_WC
        
    def IdealUtilitarianism (Values):
        # BCS
        value_BC = 0
        value_BC = Values.BC_IG / 10
        value_BC += Values.Approval / 10
        value_BC += Values.BC_CG
        # WCS
        value_WC = 0
        value_WC = Values.WC_IG / 10
        value_WC += Values.Approval / 10
        value_WC += Values.WC_CG
        value_WC /= 10
        
        return value_BC, value_WC
    
    def Egoism (Values):
        # BCS
        value_BC = 0
        value_BC = Values.BC_CG / 10
        value_BC += Values.Approval / 10
        value_BC += Values.BC_IG
        # WCS
        value_WC = 0
        value_WC = Values.WC_CG / 10
        value_WC += Values.Approval / 10
        value_WC += Values.WC_IG
        
        return value_BC, value_WC
    
    
    def MoralRelativism (CommonGood, IndividualGood, Approval, BCS = True):
        return 0
    
    
def main(): # for testing purpouses 
    Evaluate(MedicareForAll, 'Utilitarianism')
    
def Evaluate(Values, name):
    
    BCS, WCS = Ethics.Select(Values, name)

    EV = DesicionTheory.ExpectedValue(BCS, WCS, Values.Probability / 100)
    
    if EV > Values.Budget:
        print("law passes")
    else:
        print("law doesn't pass")
        
    print(EV)
         
main()