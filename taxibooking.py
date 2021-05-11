from taxi import taxi
# from taxi import allocation
from choice_print import *
from thread_taxi import holder
from threading import Thread
from time import sleep
book_no = 0
class booking():
    def __init__(self, cust_id, pick_point, drop_point, pick_time):
        self.book_no = book_no
        self.cust_id = cust_id
        self.pick_point = pick_point
        self.drop_point = drop_point
        self.pick_time = pick_time
cont = 1
choices_ = ["cust_id ", "pick_point a-f ", "droppoint a-f", "pick_time"]
if __name__ == "__main__":
    exit = 0
    taxi_list = []
    booking_list = []
    for i in range(4):
        taxi_list.append(taxi(i+1))
    while(exit != 1):
        display_choice()
        choice_var = int(input("enter the choice"))
        # choice_cal(choice_var)
        if(choice_var == 1):
            cust_id = int(input(choices_[0]))
            pick_point = input(choices_[1])
            drop_point = input(choices_[2])
            pick_time = int(input(choices_[3]))
            flag = 0
            min_ = 9999999
            cnt = 0
            min_li=[]
            for i in taxi_list:
                # print(i.curr,pick_point)
                distance = abs(ord(i.curr)-ord(pick_point))
                if(distance == 0 and i.isfree):
                    alloted = i
                    flag = 1
                    break
                else:
                    # cnt+=1
                    
                    if(min_ > distance and i.isfree):
                        min_li = []
                        min_=distance
                        min_li.append(((min_, i)))
                    elif((min_ == distance) and i.isfree):
                        min_li.append((min_, i))
                       # print("min_list",min_li)
                    #print(min_li) 
            min_bal = 999999
            
            if(flag != 1):
                for i, j in min_li:
                    if(min_bal > j.earning):
                        min_bal = j.earning
                        #print("minbal\n",min_bal,j)
                        obj = j
                if(min_bal != 999999):
                    alloted = obj
                    flag = 1
            if(flag == 1):
                print("taxi allocated-", alloted.ident)
                book_no += 1
                alloted.allocation(book_no, pick_point, drop_point, pick_time)
                # print(alloted.bookid,alloted.pick,alloted.dp)
                # time=abs(ord(pick_point)-ord(drop_point))*60
                holder(alloted, 20).start()
                sleep(1)
            else:
                print("please try after sometimes\n")
                 
        elif(choice_var==2):
          for i in taxi_list:
            print("{:10}{:10}{:10}{:10}{:10}".format(str(i.ident), str(i.pick), str(i.dp), str(i.droptime), str(i.earning)))    
        elif(choice_var == 3):
            exit = 1
        '''
            elif(choice_var==2):
            details()
            '''
    print("{:10}{:10}{:10}{:10}{:10}".format(
        "ident", "pick", "dp", "drop", "earn"))
    
