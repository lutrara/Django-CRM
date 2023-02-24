#
#
#
#
#

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '1234567'

	)

#
cursorObject = dataBase.cursor()

#
cursorObject.execute("CREATE DATABASE elett")

print("All Done")
