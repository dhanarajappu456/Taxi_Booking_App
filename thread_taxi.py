from threading import Thread 
from time import sleep  
class holder(Thread):
    
    def __init__(self,taxi_,time_):
        self.taxi_=taxi_
        self.time_=time_
        Thread.__init__(self)
    def run(self):
        
        self.taxi_.isfree=0
        sleep(self.time_)
        self.taxi_.isfree=1        
        
        
        return
        
        
    
    