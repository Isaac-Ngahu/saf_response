import psycopg2
mydb = psycopg2.connect(
"postgresql://response_user:zC02dAZUYFVEKgy8vMmh9ChaLK5fT6Vo@dpg-cq16eteehbks73er0gs0-a/response"
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