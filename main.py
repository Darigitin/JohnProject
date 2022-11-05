import os

from dotenv import load_dotenv
import json
import typing
import fmpsdk

# Actual API key is stored in a .env file.  Not good to store API key directly in script.
load_dotenv()
apikey = "8735a51bc26a3820b9363e57a36183da"

# Company Valuation Methods
symbol: str = "AAPL"
#f = open("apple.txt", "w")
#f.write(f"{fmpsdk.company_profile(apikey=apikey, symbol=symbol)}")
#f.close()

f = open("apple.txt", "r")
d = f.readline()
print(d)
#g = open("apple.json", "w")
#g.write(json.dumps(f.read()))

#with open('apple.json', 'r') as json_file:
#    json_load = json.load(json_file)

#print(json_load)
