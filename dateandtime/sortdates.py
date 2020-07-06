from datetime import date
import time
startTime=time.perf_counter()

ldates=[]
d1=date(2016,8,12)
d2=date(2018,8,12)
d3=date(2020,8,12)
d4=date(2012,8,12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.append(d4)

ldates.sort()

time.sleep(3)
for i in ldates:
    print(i)
    
endTime=time.perf_counter()
print("execution time",endTime-startTime)
