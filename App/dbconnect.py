import pymysql
import os

HOST     = os.environ.get('RDS_HOSTNAME') or 'localhost'
USER     = os.environ.get('RDS_USERNAME') or 'root'
PASSWD   = os.environ.get('RDS_PASSWORD') or 'c1o2l3d4'
DATABASE = os.environ.get('RDS_DB_NAME') or 'society_mysqldb'
PORT     = os.environ.get('RDS_PORT') or 3306
def connection():
	conn = pymysql.connect(host = HOST, user = USER, passwd = PASSWD, db = DATABASE, port = PORT)
	cursor = conn.cursor()
	return conn, cursor
