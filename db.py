import mysql.connector
mydb = mysql.connector.connect(
  host="isaacngahu.mysql.pythonanywhere-services.com",
  user="isaacngahu",
  database="isaacngahu$response",
  password="12976@pythonanywhere",
  port=3306
)

def insert_response(sender,response):
  cursor = mydb.cursor()
  try:
    sql = "INSERT INTO response (sender,reponse) VALUES (%s,%s)"
    values = (sender,response)
    cursor.execute(sql,values)
    mydb.commit()
    return True
  finally:
    cursor.close()

def get_responses():
  cursor = mydb.cursor()
  try:
    sql = "SELECT * FROM response ORDER BY TimeReceived DESC LIMIT 3"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows
  finally:
    cursor.close()


print(insert_response("safaricom","testing 2 3 4"))