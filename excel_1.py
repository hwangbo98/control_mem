import pyzbar.pyzbar as pyzbar
import cv2
import matplotlib.pyplot as plt

from openpyxl import Workbook
from datetime import datetime, timezone, date, time
from pytz import timezone, utc

KST = timezone('Asia/Seoul')

now_time = datetime.utcnow()
list_h_m_s = []
y_m_d = utc.localize(now_time).astimezone(KST).strftime("%Y-%m-%d")
print(y_m_d)

print(now_time.strftime("%Y-%m-%d"))
'''h_m_s = utc.localize(now_time).astimezone(KST).strftime("%H-%M-%d")'''
h_m_s = utc.localize(now_time).astimezone(KST).strftime("%H:%M:%S")

list_h_m_s.append(datetime.strptime(h_m_s,"%H:%M:%S"))

time_a  = '16:04:00'
print(list_h_m_s[0])

a_time = datetime.strptime(time_a,"%H:%M:%S")

diff = a_time - list_h_m_s[0] 
'''
if diff < 1 :
 print(list_h_m_s[0])

else :
 print(a_time)
'''

print(diff.total_seconds()/60)

print(h_m_s)

print(now_time.strftime("%H:%M:%S"))


'''send_excel()

def send_excel() :
        write_wb = Workbook()
        write_ws = write_wb.create_sheet('Jan,Feb')

        print(wb.sheetnames)

        write_ws = write_wb.active
        now_time = datetime.now()

	today.isoformat()

'''
