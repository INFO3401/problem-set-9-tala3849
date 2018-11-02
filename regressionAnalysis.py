#WORKED WITH MARISSA AND HANNAH ON THIS 

import pandas 
import numpy as pd 
import csv 

#PART B
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import LogisticRegression 

import matplotlib.pyplot as plt 

#PART A 
class AnalysisData:
    
    def __init__(self):
        self.dataset = [] 
        self.variables = []
        
#QUESTION 1     
    def parseFile(self, filename): 
        self.dataset = pd.read_csv(filename)
        self.variables = []
        
        for self.dataset.columns.values:
            if column != "competitorname": 
                self.variables.append(column) 


    



#PART B 
#linear analysis 

class LinearAnalysis: 
    
    def __init__(self, targetY_input): 
        self.bestX = ""
        self.targetY = targetY_input  
        self.fit = ""
        
    def runSimpleAnalysis(self, data):
        regr = LinearRegression()
        regr.fit(<candy>, <sugar>)
        regr.predict(<candy>)
        r2_score(<sugar>, <predicted values>)
    

    
#QUESTION 1             
data = AnalysisData()
data.parseFile("candy-data.csv")
        
        
        
        
#string put quotes, going to be integer put 0 or -1, dictionary are {}, lists are [] 

#PART C

#Logisitc anaylsis 

class LogisticAnalysis: 
    
    def __init__(self, targetY_input): 
        self.bestX = ""
        self.targetY = targetY_input
        self.fit = ""
        
        


#QUESTION 2 
#shown in part B and C 



#WEDNESDAY WORK 
#under part B 






