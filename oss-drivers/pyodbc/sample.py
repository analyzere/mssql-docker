import pyodbc
import os
server = os.environ['DB_HOST']
username = os.environ['DB_USERNAME']
password = os.environ['DB_PASSWORD']

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

print ('Using the following SQL Server version:')
tsql = "SELECT @@version;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    print (str(row[0]))

