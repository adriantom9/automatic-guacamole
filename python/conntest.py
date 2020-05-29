import time
import datetime
import mysql.connector
import random

n = 0
cnt = 0

unit = ['temp', 'hum', 'wt', 'flow', 'ph', 'ec']
loc = ['cs1', 'cs2']

while n == 0:
	
	dt = datetime.datetime.now()
	dts = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day) + "-" + str(dt.hour - 1)
	dtmin = dt.min
	
	if dtmin == 0 and cnt == 0:
	#if cnt == 0:
		cnx = mysql.connector.connect(host='localhost', user='citaitb', passwd='dbc1t4', database='hydrotest')
		cursor = cnx.cursor()

		r1 = random.random() * 5 + 25
		r2 = random.random() * 20 + 60
		r3 = random.random() * 5 + 23
		r4 = random.random() * 5 + 5
		r5 = random.random() + 6.5
		r6 = random.random() * 1000 + 1500

		query = ("INSERT INTO avgdummytable(datetime, temp, hum, wt, flow, ph, ec) VALUES ('" + 
		dts + "','" +
		str(r1) + "','" +
		str(r2) + "','" +
		str(r3) + "','" +
		str(r4) + "','" +
		str(r5) + "','" +
		str(r6) + "')")
		#print(query)
		
		cursor.execute(query)
		
		print("entried")

		cnx.commit()
		
		cursor.close()
		cnx.close()
		cnt = cnt+1
	if dtmin > 0: cnt = 0
	time.sleep(0.02)
