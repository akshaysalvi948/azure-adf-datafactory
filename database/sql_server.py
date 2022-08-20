
	
import psycopg2	

class DbConnections():
	self.username = dbutils.secrets.get(scope = "mysecret", key = "Postgres-username")
	self.password = dbutils.secrets.get(scope = "mysecret", key = "Postgres-password")
	self.db_name = dbutils.secrets.get(scope = "mysecret", key = "Postgres-dbname")
	self.host_name = dbutils.secrets.get(scope = "mysecret", key = "Postgres-hostname")

def mssql_conn(self):


	conn_string = f"host={host_name} dbname={db_name} user={username} password={password}"
	print(conn_string)
	conn = psycopg2.connect(conn_string)
	#conn = print("Hi am in")
	print(conn)
	return conn

