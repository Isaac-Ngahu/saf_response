import psycopg2
mydb = psycopg2.connect(
  host="dpg-cq16eteehbks73er0gs0-a",
  user="response_user",
  database="response",
  password="zC02dAZUYFVEKgy8vMmh9ChaLK5fT6Vo",
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


print(insert_response("safaricom","testing..."))