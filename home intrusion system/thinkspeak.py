import requests 
from datetime import datetime
t=datetime.now().strftime('%H:%M:%S')
URL ="https://api.thingspeak.com/update?api_key=Y2BK82L6M5WJOEDF&field1="+t
r = requests.get(url = URL)
print(r)
