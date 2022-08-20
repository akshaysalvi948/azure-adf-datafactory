from database.sql_server import DbConnections
conn = DbConnections().mssql_conn()
print(conn)