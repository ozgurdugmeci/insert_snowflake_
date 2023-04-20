import snowflake.connector
import pandas as pd
yol='C:\\Users\\ozgur.dugmeci\\AppData\\Local\\Programs\\Python\\Python37\\sales.xlsx'

df= pd.read_excel (yol,'Sayfa1')


df2=df.head(5)

df= df.values.tolist()




#connection lines 

cur = conn.cursor()
insert_query = f"INSERT INTO SALES3 (PRODUCT,Inventory ,SALES_20, SALES_40, SALES_60,SALES_80) VALUES (%s, %s, %s, %s,%s,%s)"
cur.executemany(insert_query,df)
conn.commit()

# Close the connection
conn.close()

 
'''def basla():
 x=151
 y=15
 return x,2*y
 
if __name__ == "__main__":
 basla()  
 
print(__name__)'''
