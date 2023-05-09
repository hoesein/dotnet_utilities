import http.client
from datetime import datetime
import json

now = datetime.now()
timestamp = now.strftime("%Y%m%d%H%M%S")
auth = f""
base_address = ""
base_port = ""

conn = http.client.HTTPConnection(base_address, base_port)
payload = json.dumps({
    
    })
headers = {
        'Authorization': "",
        'Content-Type': 'application/json',
        'Accept': 'application/json'
        }
conn.request("GET", "endpoint", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))