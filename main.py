import os

#from dotenv import load_dotenv
import psycopg2
import json
import typing
import fmpsdk

# Actual API key is stored in a .env file.  Not good to store API key directly in script.
#load_dotenv()
apikey = "8735a51bc26a3820b9363e57a36183da"

conn = psycopg2.connect(
    database="postgres",
    user='postgres',
    password='password',
    host='localhost',
    port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

# sql = '''CREATE TABLE COMPANYPROFILE(symbol char(20) NOT NULL,\
#          price float, beta float, volAvg int, mktCap bigint, \
#          lastDiv float, range char(100), changes float, \
#          companyName char(50), cik char(50), isin char(50), \
#          exchange char(50), exchangeShortName char(10), \
#          industry char(50), description char(8000), sector char(20), country char(10));'''

#cursor.execute(sql)
# Company Valuation Methods
symbol: str = "AAPL"
d = fmpsdk.company_profile(apikey=apikey, symbol=symbol)

print(d)

#columns=d.keys()
#print(columns)

#g = open("apple.json", "w")
#g.write(json.dumps(f.read()))

#with open('apple.json', 'r') as json_file:
#    json_load = json.load(json_file)

#print(json_load)
