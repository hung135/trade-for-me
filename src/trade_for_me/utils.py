import pprint 

class CircularQueQue:
    
    def __init__(self,length,value=0):
        self.list=[]
        
        self.length=length
        self.pos=0
        self.highest=None
        self.lowest=None
        
    def add(self,value:float):
        value=float(value)
        if len(self.list)<self.length:
            self.list.append(value)
        self.list[self.pos]=value

        if  self.highest is None or value>self.highest:
            self.highest=value

        if  self.lowest is None or value<self.lowest:
            self.lowest=value
        if self.pos+1>=self.length:
            self.pos=0
        else:
            self.pos+=1
    def avg(self):
        
        return sum(self.list) / (len(self.list))
    
from os import system, name 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')