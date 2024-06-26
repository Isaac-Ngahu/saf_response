import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="penzi",
  port=3306,
  password="12976"
)

def insert_response(sender,response):
  cursor = mydb.cursor()
  try:
    sql = "INSERT INTO response (sender,reponse) VALUES (%s,%s)"
    values = (sender,response)
    cursor.execute(sql,values)
    mydb.commit()
  finally:
    cursor.close()