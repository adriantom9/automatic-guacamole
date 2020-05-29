import mysql.connector
from mysql.connector import Error

def con(host_name, user_name, user_password, db):
	conn = None
	try:
		conn = mysql.connector.connect(
			host=host_name,
			user=user_name,
			passwd=user_password,
			database=db
		)
		print("koneksi sukses anjing")
	except Error as e:
		print("yeah anjing gagal")
	return conn

conn = con("localhost", "citaitb", "dbc1t4","hydrotest")


