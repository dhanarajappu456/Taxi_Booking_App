from threading import Thread
from thread_taxi import holder
class taxi:
 
 
 def __init__(self,ident_):
       self.earning=0
       self.ident=ident_
       self.curr="a" 
       self.isfree=1
       self.bookid=[]
       self.dp=[]
       self.pick=[]
       self.picktime=[]
       self.droptime=[]
  
 
 def allocation(self,book_id,pick,dest,picktime):
       self.earning+=(10*((abs((ord(dest)-ord(pick)))*15)-5))+100
       self.bookid.append(book_id)
       self.dp.append(dest)
       self.pick.append(pick)
       self.picktime=picktime
       self.curr=dest
       self.droptime.append(abs(ord(pick)-ord(dest))*60)
       return
       #print(self.dp,self.pick)
       
       
       
       
       
       
       
       
       


