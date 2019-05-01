#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:19:13 2019

@author: f
"""



class DesicionTheory ():
    def ExpectedValue (BCS, WCS, Probability):
        return ((BCS * Probability)+(WCS * (1 - Probability)))        
    
class Ethics (): 
    def Utilitarianism (CommonGood, IndividualGood, Approval, BCS = True):
        value = 0
        IndividualGood /= 10
        Approval /= 10
        value = CommonGood + IndividualGood + Approval 
        return value
        
    def Egoism (CommonGood, IndividualGood, Approval, BCS = True):
        value = 0    
        CommonGood /= 10
        Approval /= 10
        value = IndividualGood + CommonGood + Approval       
        return value
        
    def IdealUtilitarianism (CommonGood, IndividualGood, Approval, BCS = True):
        value = Ethics.Utilitarianism(CommonGood, IndividualGood, Approval)
        if BCS != True:    
            return value / 10
        return value

    
    
def main(): # for testing purpouses 
    # Medicare for all
    Budget = 20
    Probability = 90
    Approval = 50
    BCS_CG = 100
    BCS_IG = -20
    WCS_CG = 50
    WCS_IG = -90
    
    
    BCS = Ethics.IdealUtilitarianism(BCS_CG, BCS_IG, Approval, True)
    WCS = Ethics.IdealUtilitarianism(WCS_CG, WCS_IG, Approval, False)
    
    EV = DesicionTheory.ExpectedValue(BCS, WCS, Probability / 100)
    
    if EV > Budget:
        print("law passes")
    else:
        print("law doesn't pass")
        
    print(EV)
         
main()