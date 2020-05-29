import datetime
import mysql.connector

unit = ['temp', 'hum', 'wt', 'flow', 'ph', 'ec']
loc = ['cs1', 'cs2']

dt = datetime.datetime.now()
print(dt)
print(type(dt))
print(dt.month)
print(type(dt.month))
dts = str(dt.year) + "-" + str(dt.month) + "-" + str(dt.day) + "-" + str(dt.hour - 1)
print(dts)

cnx = mysql.connector.connect(host='localhost', user='citaitb', passwd='dbc1t4', database='hydrotest')
cursor = cnx.cursor()

for a in loc:
	for b in unit:
		query = "SELECT AVG(val) AS avgval FROM " + a + " WHERE unit='" + b + "'AND datetime='" + dts +"'"
		cursor.execute(query)
	
	
		for avgval in cursor:
			valt = avgval
	
	
		val = valt[0]
		print("{} unit:{} value:{}".format(a, b, val))

cursor.close()
cnx.close()
