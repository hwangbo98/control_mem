import getpass
import pickle
import os
import sys
from openpyxl import load_workbook
from openpyxl import Workbook
import openpyxl
from datetime import datetime, timezone, date, time
from pytz import timezone, utc

def register(data) :
	
	x = input("Do you want to register? :")
	x_lower = x.lower()
	if x_lower == 'yes':
		while(1) :
			account = input("Which ID do you want? :")
			if account in data.keys() :
				print("already exist")
			else :
				password = getpass.getpass("which password do you want? :") 
				break
		
	else :
		pass

	data[account] = password
	with open('account.pkl', 'wb') as account_file :
		pickle.dump(data,account_file)
	print(account) 
	print(password)
	return data
def login(data) :
	while(1) :
		id_input = input("Write the ID :")
		pw_input = getpass.getpass("Write the PW :")

		if id_input in data :
			if data[id_input] == pw_input :
				print("Login Success")
				break
			else :
				print("Password Wrong")

		else :
			print("rewrite the ID & PW")

	return id_input
def time_service(id_info) :
	KST = timezone('Asia/Seoul') #ubuntu default UTC Time
	split_day_time =[]
	list_h_m_s = []
	now_time = datetime.utcnow()
	timeTostr = utc.localize(now_time).astimezone(KST).strftime("%Y-%m-%d %H:%M:%S")
	strToint = datetime.strptime(timeTostr,"%Y-%m-%d %H:%M:%S")
	split_day_time = strToint.strftime("%Y-%m-%d %H:%M:%S").split()
	print(split_day_time[0])
	print(split_day_time[1])
	split_day_time.append(id_info)
	print(split_day_time[2])
	return split_day_time

def handle_excel(id_info) :
	wb = openpyxl.load_workbook("work_sheet.xlsx",data_only = True)		
	now_sheet = wb.get_sheet_by_name(id_info)
	
id_pw = dict()
day_time_name = []
filesize = os.path.getsize('account.pkl')
if filesize == 0 :
	pass
else :	
	with open('account.pkl', 'rb') as fin :
		id_pw = pickle.load(fin)
print("You must choice the number, What do you want?")
choice = input("1.register 2.login 3.logout " )
if choice == "1" :
	id_pw = register(id_pw)
elif choice == "2" :
	who_am_i = login(id_pw)
	answer = int(input("1. go to work 2. leave the office :"))
	if answer == 1 :
		day_time_name = time_service(who_am_i)
	elif answer == 2 :
		day_time_name = time_service(who_am_i)	
elif choice == "3" :
	sys.exit()
