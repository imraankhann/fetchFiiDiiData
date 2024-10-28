import time
from pytz import timezone
from datetime import datetime
import os 


now = datetime.now()
format = "%d-%m-%Y %H:%M:%S %Z%z"
now_utc = datetime.now(timezone('UTC'))
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
ocTime = now_asia.strftime(format)
fName = now_asia.strftime(format)
tdate = fName.split(" IST")
nowTime = tdate[0]
print(nowTime)
curWeekday = datetime.today().weekday()
dtTime = fName.split(" IST")
dt = dtTime[0].split(" ")
reqTime = ocTime[11:16]
intTime = int(reqTime[0:2])
dtWithOutTime = dt[0].split(" ")
dateWithOutTime = dtWithOutTime[0]
logFileName = dateWithOutTime+"-"+"MagicLevel.log"

file_path = logFileName
if(intTime>22 and os.path.exists(logFileName)):
    os.remove(logFileName)
else:
    print("The log file does not exist or time not reached to deleted as the time is : ",intTime)
