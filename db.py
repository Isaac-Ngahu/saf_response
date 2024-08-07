import psycopg2
mydb = psycopg2.connect(
"postgresql://response_user:zC02dAZUYFVEKgy8vMmh9ChaLK5fT6Vo@dpg-cq16eteehbks73er0gs0-a/response"
)

def insert_response(sender,response):
  cursor = mydb.cursor()
  try:
    sql = "INSERT INTO saf_response (sender,message) VALUES (%s,%s)"
    values = (sender,response)
    cursor.execute(sql,values)
    mydb.commit()
    return True
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    return error
  finally:
    cursor.close()

def get_responses():
  cursor = mydb.cursor()
  try:
    sql = "SELECT * FROM saf_response ORDER BY timereceived DESC"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    return error
  finally:
    cursor.close()
