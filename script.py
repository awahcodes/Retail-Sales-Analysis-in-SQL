import pandas as pd  
from sqlalchemy import create_engine 

conn_string = 'postgresql://postgres:Onajourney123#@localhost/walmart'
db = create_engine(conn_string)
conn = db.connect()

df = pd.read_csv('C:/Users/aniwa/OneDrive/Desktop/New World/Data Analyst Portfolio/Walmart Sales Analysis SQL/walmartsalesdata.csv')
print(df.info)


df.to_sql('walmartsalesdata', con=conn, if_exists='replace', index=False)


