from datetime import *
from dateutil.relativedelta import *
from pytz import timezone

now = datetime.now(timezone('Asia/Seoul'))
now_s = now.strftime("%Y-%m-%d")
now_i = datetime.strptime(now_s, "%Y-%m-%d")
#year, month, day = 2021, 4, 20
print(now)
goal_day = input("you should type the day ex) 1970-01-01 : ")

goal_day_s = datetime.strptime(goal_day, "%Y-%m-%d")

delta = goal_day_s - now_i
#d_day = relativedelta(now, datetime(year, month, day))
print( "%s day" %(delta.days))


