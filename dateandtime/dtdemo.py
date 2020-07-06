import time,datetime

epochsecounds=time.time()
print(epochsecounds)

t=time.ctime(epochsecounds)
print(t)

dt=datetime.datetime.today()
print("current date: {}/{}/{}".format(dt.day,dt.month,dt.year))
print("current time: {}:{}:{}".format(dt.hour,dt.minute,dt.second))








