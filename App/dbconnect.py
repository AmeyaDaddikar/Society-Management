import pymysql
import os

HOST     = os.environ.get('DB_HOST') or 'localhost'
USER     = os.environ.get('DB_USER') or 'root'
PASSWD   = os.environ.get('DB_PASSWD') or 'c1o2l3d4'
DATABASE = os.environ.get('DB_DATABASE') or 'society_mysqldb'
def connection():
	conn = pymysql.connect(host = HOST, user = USER, passwd = PASSWD, db = DATABASE)
	cursor = conn.cursor()
	return conn, cursor
