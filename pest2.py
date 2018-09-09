# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:48:14 2018

@author: ashut
"""

import datetime
import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta
start = datetime.datetime.strptime(input(" Please Enter the Season Start Date(MM/DD):"),"%m/%d")
stmonth,stdate= list(start.timetuple())[1:3]
end = datetime.datetime.strptime(input(" Please Enter the Season End Date(MM/DD):"),"%m/%d")
enmonth,endate= list(end.timetuple())[1:3]
freq= int(input(" Please Enter the frequency(number of days):"))
last_service = datetime.datetime.strptime(input(" Please Enter the last service Date(MM/DD/YYYY):"),"%m/%d/%Y")
lyear,lmonth,ldate = list(last_service.timetuple())[0:3]
servicemd = datetime.datetime.strptime((str(lmonth)+"/"+str(ldate)),"%m/%d")
num= int(input(" Amount of upcoming services to be calculated :"))

def season_time(start,end,enmonth,endate,stmonth,stdate):
    if start<end:
        return (enmonth-stmonth) ,(endate-stdate)
    else:
        return (12-abs(enmonth-stmonth)) , (endate-stdate)

def relevant_dates(start,end,servicemd,lyear,enmonth,endate,stmonth,stdate):
    start_year = 0
    if start<end:
        if servicemd<end:
            start_year = lyear
        else:
            start_year = lyear + 1
    else:
        if servicemd<end:
            start_year = lyear -1
        else:
            start_year = lyear
    start_date = datetime.datetime.strptime((str(stmonth)+"/"+str(stdate) + "/" + str(start_year)),"%m/%d/%Y")
    mons,day = season_time(start,end,enmonth,endate,stmonth,stdate)
    
    end_date = start_date + relativedelta(months= mons, days = day)
    return start_date,end_date


def main_function(start, end, freq, last_service, num):
    service_counter = num
    date_list =[]
    
     
    stmonth,stdate= list(start.timetuple())[1:3]
    enmonth,endate= list(end.timetuple())[1:3]
    
    lyear,lmonth,ldate = list(last_service.timetuple())[0:3]
    servicemd = datetime.datetime.strptime((str(lmonth)+"/"+str(ldate)),"%m/%d")
    start_date, end_date = relevant_dates(start,end,servicemd,lyear,enmonth,endate,stmonth,stdate)
    pivot = start_date
    cursor = last_service
    
         
     
    while service_counter>0:
        if cursor.year == pivot.year:
            
            if cursor< start_date: ##last service format
                cursor  = start_date + relativedelta( days = last_service.day - start_date.day)
                date_list.append(cursor)
            
            
            elif ((cursor>= start_date) & (cursor<=(end_date - relativedelta( days = freq)))):
            
                cursor += relativedelta( days = freq)
                date_list.append(cursor)
            
            elif((cursor>(end_date - relativedelta( days = freq))) & (cursor<(end_date - relativedelta( days = (freq/2))))):
            
                cursor = end_date
                date_list.append(cursor)
            elif(cursor>=(end_date - relativedelta( days = (freq/2)))):
            
                start_date = start_date + relativedelta( years = 1)
                end_date = end_date + relativedelta( years = 1)
                cursor = start_date
                date_list.append(cursor)
        elif cursor.year != pivot.year:
            if cursor< start_date: ##last service format
                cursor  = start_date 
                date_list.append(cursor)
            
            
            elif ((cursor>= start_date) & (cursor<=(end_date - relativedelta( days = freq)))):
            
                cursor += relativedelta( days = freq)
                date_list.append(cursor)
            
            elif((cursor>(end_date - relativedelta( days = freq))) & (cursor<(end_date - relativedelta( days = (freq/2))))):
            
                cursor = end_date
                date_list.append(cursor)
            elif(cursor>=(end_date - relativedelta( days = (freq/2)))):
            
                start_date = start_date + relativedelta( years = 1)
                end_date = end_date + relativedelta( years = 1)
                cursor = start_date
                date_list.append(cursor)
        service_counter = service_counter-1
    return date_list
                
k =  main_function(start, end, freq, last_service, num)
print(k)
            
            
         
    
    
    


