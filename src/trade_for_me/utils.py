import pprint 

class CircularQueQue:
    
    def __init__(self,length,value=0):
        self.a=[]
        
        self.length=length
        self.pos=0
        
    def add(self,value):
        
        if len(self.a)<self.length:
            self.a.append(float(value))
        self.a[self.pos]=float(value)
        if self.pos+1>=self.length:
            self.pos=0
        else:
            self.pos+=1
    def avg(self):
        
        return sum(self.a) / len(self.a)
   