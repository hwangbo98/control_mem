from datetime import *
from pytz import timezone

now = datetime.now(timezone('Asia/Seoul'))
now_s = now.strftime("%Y-%m-%d")
now_i = datetime.strptime(now_s, "%Y-%m-%d")
goal_day = input("you should type the day ex) 1970-01-01 : ")

goal_day_s = datetime.strptime(goal_day, "%Y-%m-%d")

delta = goal_day_s - now_i
print( "%s day" %(delta.days))
deltaToint = delta.days
if deltaToint%3 == 0 :
	day_time = deltaToint//3
	night_time = deltaToint//3
	first_night = deltaToint//3
elif deltaToint%3 == 1 :
	day_time = deltaToint//3 + 1
	first_night = deltaToint//3 
	night_time = deltaToint//3
else :
	day_time = deltaToint//3 + 1
	first_night = deltaToint//3 + 1
	night_time = deltaToint//3

print(day_time) 
print(" you have {}nighttime, {}firstnight, {}daytime".format(night_time,first_night,day_time))
print(type(deltaToint))
