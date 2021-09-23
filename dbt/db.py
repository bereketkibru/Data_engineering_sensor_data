import mysql.connector as mysql
from sqlalchemy import create_engine, types
import pandas as pd
import os


SENSOR_DATA = 'SensorData'


class Create_DWH:

  def __init__(self, host: str, user: str, passwd: str) -> None:
      self.conn, self.cur = self.connect(host, user, passwd)

  
  def connect(self, host: str, user: str, passwd: str, dbName: str = "SensorData"):
  
    try:
      
      conn = mysql.connect(host=host, user=user, password=passwd,
                          database=dbName, buffered=True)
      return conn, conn.cursor()

    except Exception as ex:

      conn = mysql.connect(host=host, user=user, password=passwd, buffered=True)

      cur = conn.cursor() 
      sql = f"CREATE DATABASE {SENSOR_DATA}"

      cur.execute(sql)
      return conn, cur
  
  def insertData(self, dbName: str,  host: str, user: str, password: str, tableName: str, csv_file: str):
        engine = create_engine(
            f'mysql+pymysql://{user}:{password}@{host}/{dbName}')

        df = pd.read_csv(csv_file, sep=',', quotechar='\'', encoding='utf8')
        df.to_sql(tableName, con=engine, index=False, if_exists='append')



  
if __name__ == "__main__":

  TABLE_NAME = "observation"
  a = Create_DWH(host = "localhost", user = "root", passwd = "root")
  a.insertData(SENSOR_DATA, "localhost", "root", "root", TABLE_NAME, "./data/sample2.txt" )