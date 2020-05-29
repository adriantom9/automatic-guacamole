import time
import datetime
import mysql.connector

n = 0
cnt = 0

unit = ['temp', 'hum', 'wt', 'flow', 'ph', 'ec']
loc = 'dumdum'
r = [ '', '', '', '', '', '']

while n == 0:
	dt = datetime.datetime.now()
	dts = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day) + "-" + str(dt.hour - 1)
	dtmin = dt.minute	

#	if n == 0:
	if dtmin == 0 and cnt == 0:
		cnx = mysql.connector.connect(host='localhost', user='citaitb', passwd='dbc1t4', database='hydrotest')
		cursor = cnx.cursor()

		cntb = 0
		for b in unit:
			query = "SELECT AVG(val) AS avgval FROM " + loc + " WHERE unit='" + b + "'AND datetime='" + dts +"'"
			cursor.execute(query)
			for avgval in cursor:
				valt = avgval

			val = valt[0]
			r[cntb] = val
			print("cntb: {}, val: {}, result: {}".format(cntb, val, r[cntb]))
				
				#print("{} unit:{} value:{}".format(a, b, val))
			cntb = cntb + 1
		
		query2 = ("INSERT INTO avgdummytable(datetime, temp, hum, wt, flow, ph, ec) VALUES ('" +
		dts + "','" +
		str(r[0]) + "','" +
		str(r[1]) + "','" +
		str(r[2]) + "','" +
		str(r[3]) + "','" +
		str(r[4]) + "','" +
		str(r[5]) + "')")
		
		cursor.execute(query2)
		print("entried")
		
		cnx.commit()

		cursor.close()
		cnx.close()
		cnt = cnt + 1

	
	if dtmin > 0: cnt = 0
	time.sleep(0.02)
