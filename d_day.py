from datetime import *
from pytz import timezone

now = datetime.now(timezone('Asia/Seoul'))
now_s = now.strftime("%Y-%m-%d")
now_i = datetime.strptime(now_s, "%Y-%m-%d")
goal_day = input("you should type the day ex) 1970-01-01 : ")

goal_day_s = datetime.strptime(goal_day, "%Y-%m-%d")

delta = goal_day_s - now_i
print( "%s day left!" %(delta.days))
deltaToint = delta.days
if deltaToint%4 == 0 :
	day_time = deltaToint//4
	night_time = deltaToint//4 + 1
	first_night = deltaToint//4
	free_time = deltaToint//4
elif deltaToint%4 == 1 : 
	day_time = deltaToint//4 
	first_night = deltaToint//4 + 1
	night_time = deltaToint//4 + 1
	free_time = deltaToint//4
elif deltaToint%4 == 2 : 
	day_time = deltaToint//4 + 1
	first_night = deltaToint//4 + 1
	night_time = deltaToint//4 + 1
	free_time = deltaToint//4 
else :
	day_time = deltaToint//4 + 1
	first_night = deltaToint//4 + 1
	night_time = deltaToint//4 + 1
	free_time = deltaToint//4 + 1

print(day_time) 
print("you have {}nighttime, {}firstnight, {}daytime, {}freetime".format(night_time,first_night,day_time,free_time))
print(type(deltaToint))
