#urlopen
#'getheader'
# 'status
import urllib.request
import json

url = f'https://api.github.com/users/rscopim/events'
res = urllib.request.urlopen(url)

response = json.loads(res.read().decode('utf-8'))
print(response)