import MySQLdb

HOST     = 'localhost'
USER     = 'root'
PASSWD   = 'c1o2l3d4'
DATABASE = 'society_mysqldb'
def connection():
	conn = MySQLdb.connect(host = HOST, user = USER, passwd = PASSWD, db = DATABASE)
	cursor = conn.cursor()
	return conn, cursor
